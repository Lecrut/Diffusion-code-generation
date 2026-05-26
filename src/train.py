from functools import partial
import gc
import threading
import queue as _queue
import time
from pathlib import Path
import os
import shutil
import random
import math
import tempfile
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv

from diffusion.model import LocalConvDiffCoder
from tokenizer import CodeTokenizer 

try:
    from comet_ml import Experiment
except Exception:
    Experiment = None


def clear_comet_temp_cache() -> None:
    cache_roots = [
        Path(os.path.expanduser("~/.cometml")),
        Path(os.path.expanduser("~/.comet_offline")),
    ]
    temp_root = Path(tempfile.gettempdir())

    for cache_root in cache_roots:
        try:
            if cache_root.exists():
                shutil.rmtree(cache_root, ignore_errors=True)
        except Exception:
            pass

    if temp_root.exists():
        for entry in temp_root.iterdir():
            name = entry.name.lower()
            if "comet" in name:
                try:
                    if entry.is_dir():
                        shutil.rmtree(entry, ignore_errors=True)
                    else:
                        entry.unlink(missing_ok=True)
                except Exception:
                    pass


def release_training_memory() -> None:
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        try:
            torch.cuda.ipc_collect()
        except Exception:
            pass


def log_best_model_to_comet(experiment, checkpoint_path: Path) -> None:
    if experiment is None:
        return

    print(f"Comet ML: wysyłam najlepszy model z {checkpoint_path.name}")
    clear_comet_temp_cache()
    experiment.log_model(
        name="diffcoder_best",
        file_or_folder=str(checkpoint_path),
        overwrite=True,
    )

    flush = getattr(experiment, "flush", None)
    if callable(flush):
        try:
            flush()
        except Exception:
            pass

    clear_comet_temp_cache()
    release_training_memory()


def _comet_uploader_worker(experiment, q: _queue.Queue, stop_event: threading.Event, keep_last: int = 3):
    while not stop_event.is_set() or not q.empty():
        try:
            checkpoint_path, epoch_num = q.get(timeout=1)
        except Exception:
            continue

        try:
            print(f"[COMET-UPLOADER] Rozpoczynam upload epoki {epoch_num}: {checkpoint_path.name}")
            clear_comet_temp_cache()
            experiment.log_model(name="diffcoder_best", file_or_folder=str(checkpoint_path), overwrite=True)
            clear_comet_temp_cache()
            release_training_memory()
            print(f"[COMET-UPLOADER] Upload epoki {epoch_num} zakończony.")

            # Prune old epoched checkpoints, keep only the newest `keep_last`
            parent = checkpoint_path.parent
            candidates = list(parent.glob("diffcoder_best_epoch_*.pt"))
            def _epoch_of(p):
                try:
                    return int(p.stem.split("_")[-1])
                except Exception:
                    return -1

            candidates_sorted = sorted(candidates, key=_epoch_of)
            to_delete = candidates_sorted[:-keep_last] if len(candidates_sorted) > keep_last else []
            for old in to_delete:
                try:
                    old.unlink()
                    print(f"[COMET-UPLOADER] Usunięto stary checkpoint: {old.name}")
                except Exception:
                    pass

        except Exception as e:
            print(f"[COMET-UPLOADER] Błąd podczas uploadu: {e}")
        finally:
            try:
                q.task_done()
            except Exception:
                pass


# Globals for uploader
_comet_uploader_queue = None
_comet_uploader_thread = None
_comet_uploader_stop_event = None


def prune_local_checkpoints(checkpoint_dir: Path, keep_last: int = 3):
    try:
        candidates = list(checkpoint_dir.glob("diffcoder_best_epoch_*.pt"))
        def _epoch_of(p):
            try:
                return int(p.stem.split("_")[-1])
            except Exception:
                return -1
        candidates_sorted = sorted(candidates, key=_epoch_of)
        to_delete = candidates_sorted[:-keep_last] if len(candidates_sorted) > keep_last else []
        for old in to_delete:
            try:
                old.unlink()
                print(f"[PRUNE] Usunięto lokalny stary checkpoint: {old.name}")
            except Exception:
                pass
    except Exception as e:
        print(f"[PRUNE] Błąd podczas przycinania lokalnych checkpointów: {e}")


class CodeInstructionDataset(Dataset):
    def __init__(
        self,
        csv_file,
        tokenizer,
        max_prompt_len=128,
        max_code_len=1024,
        dataset_fraction=1.0,
        seed=42,
    ):
        self.df = pd.read_csv(csv_file)
        self.df = self.df[['instruction', 'code']].dropna()
        if not (0.0 < dataset_fraction <= 1.0):
            raise ValueError("dataset_fraction must be in (0.0, 1.0].")
        if dataset_fraction < 1.0:
            keep = max(1, int(len(self.df) * dataset_fraction))
            self.df = self.df.sample(n=keep, random_state=seed).reset_index(drop=True)
        self.tokenizer = tokenizer
        self.max_prompt_len = max_prompt_len
        self.max_code_len = max_code_len
        self.pad_id = self.tokenizer.pad_token_id

    def __len__(self):
        return len(self.df)

    def _pad_or_truncate(self, ids, max_len):
        if len(ids) > max_len:
            return ids[:max_len]
        return ids

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        
        prompt_ids_raw = self.tokenizer.encode_instruction(row['instruction'])
        code_ids_raw = self.tokenizer.encode_code(row['code'])
        
        prompt_ids = self._pad_or_truncate(prompt_ids_raw, self.max_prompt_len)
        code_ids = self._pad_or_truncate(code_ids_raw, self.max_code_len)
        
        return {
            'prompt_ids': prompt_ids,
            'code_ids': code_ids
        }


def collate_batch(batch, pad_id, max_prompt_len, max_code_len):
    prompt_max = min(max(len(item['prompt_ids']) for item in batch), max_prompt_len)
    code_max = min(max(len(item['code_ids']) for item in batch), max_code_len)

    prompt_tensors = []
    code_tensors = []
    for item in batch:
        prompt_ids = item['prompt_ids'][:prompt_max]
        code_ids = item['code_ids'][:code_max]

        prompt_pad = prompt_max - len(prompt_ids)
        code_pad = code_max - len(code_ids)

        if prompt_pad > 0:
            prompt_ids = prompt_ids + [pad_id] * prompt_pad
        if code_pad > 0:
            code_ids = code_ids + [pad_id] * code_pad

        prompt_tensors.append(torch.tensor(prompt_ids, dtype=torch.long))
        code_tensors.append(torch.tensor(code_ids, dtype=torch.long))

    return {
        'prompt_ids': torch.stack(prompt_tensors, dim=0),
        'code_ids': torch.stack(code_tensors, dim=0)
    }


def log_generated_samples(model, tokenizer, samples, device, epoch, steps=50, experiment=None):
    model.eval()
    table_rows = []
    for idx, sample in enumerate(samples):
        prompt = sample["instruction"]
        target_code = sample["code"]
        prompt_ids = torch.tensor(tokenizer.encode_instruction(prompt), dtype=torch.long).to(device)
        with torch.no_grad():
            gen_ids = model.generate(
                prompt_ids,
                steps=steps,
                device=device,
                eos_token_id=tokenizer.eos_token_id,
            )
        gen_text = tokenizer.decode(gen_ids[0].tolist())

        if experiment is not None:
            experiment.log_text(
                "Epoch "
                f"{epoch} | sample {idx}\nPROMPT:\n{prompt}"
                f"\n\nGROUND_TRUTH:\n{target_code}"
                f"\n\nGENERATED:\n{gen_text}",
                step=epoch,
            )
            table_rows.append(
                {
                    "epoch": epoch,
                    "sample": idx,
                    "prompt": prompt,
                    "ground_truth": target_code,
                    "generated": gen_text,
                }
            )
        else:
            print("-" * 80)
            print(f"Epoch {epoch} | sample {idx}")
            print("PROMPT:")
            print(prompt)
            print("GROUND_TRUTH:")
            print(target_code)
            print("GENERATED:")
            print(gen_text)

    if experiment is not None and table_rows:
        experiment.log_table("generated_samples", table_rows, step=epoch)

    model.train()


def train_diffcoder(
    model,
    train_dataloader,
    val_dataloader,
    optimizer,
    scheduler,
    epochs,
    accumulation_steps,
    early_stopping_patience,
    device,
    tokenizer,
    sample_pairs,
    checkpoint_dir,
    experiment=None,
    start_epoch=0,
    best_val_loss=None,
    best_checkpoint_path=None,
):
    use_amp = device == "cuda"
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp)
    if best_val_loss is None:
        best_val_loss = float("inf")
    epochs_without_improvement = 0
    
    for epoch in range(start_epoch, epochs):
        print(f"\n[TRAIN] Start epoki {epoch + 1}/{epochs}")
        model.train()
        total_loss = 0
        progress_bar = tqdm(enumerate(train_dataloader), total=len(train_dataloader), desc=f"Epoka {epoch+1}/{epochs}")
        optimizer.zero_grad()
            
        for batch_idx, batch in progress_bar:
            x_0 = batch['code_ids'].to(device)
            prompt_ids = batch['prompt_ids'].to(device)
                
            batch_size, seq_len = x_0.shape

            u = torch.rand(batch_size, device=device)
            mask_prob = torch.cos(u * math.pi / 2)
            mask_prob = mask_prob.view(batch_size, 1)
            t = mask_prob.view(-1)
            rand_matrix = torch.rand(batch_size, seq_len, device=device)
                
            is_masked = (rand_matrix < mask_prob) & (x_0 != model.pad_token_id)
            x_t = x_0.clone()
            x_t[is_masked] = model.mask_token_id
                
            with torch.amp.autocast("cuda", enabled=use_amp):
                logits = model(x_t, prompt_ids, t)
                    
                masked_logits = logits[is_masked] 
                masked_targets = x_0[is_masked]
                    
                if masked_targets.numel() > 0:
                    loss = F.cross_entropy(masked_logits, masked_targets)
                else:
                    loss = torch.tensor(0.0, device=device, requires_grad=True)
                
            current_loss = loss.item()
            loss = loss / accumulation_steps
                
            scaler.scale(loss).backward()
                
            if (batch_idx + 1) % accumulation_steps == 0 or (batch_idx + 1) == len(train_dataloader):
                scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                scaler.step(optimizer)
                scaler.update()
                optimizer.zero_grad()
                
            total_loss += current_loss
            progress_bar.set_postfix({'loss': f"{current_loss:.4f}"})
            if experiment is not None:
                step = epoch * len(train_dataloader) + batch_idx
                experiment.log_metric("train_loss", current_loss, step=step)
                
        avg_loss = total_loss / len(train_dataloader)
        print(f"[VALIDATION] Start walidacji dla epoki {epoch + 1}")
        model.eval()
        val_total_loss = 0.0
        val_steps = 0
        with torch.no_grad():
            for val_batch in val_dataloader:
                x_0 = val_batch['code_ids'].to(device)
                prompt_ids = val_batch['prompt_ids'].to(device)
                batch_size, seq_len = x_0.shape

                u = torch.rand(batch_size, device=device)
                mask_prob = torch.cos(u * math.pi / 2)
                mask_prob = mask_prob.view(batch_size, 1)
                t = mask_prob.view(-1)
                rand_matrix = torch.rand(batch_size, seq_len, device=device)

                is_masked = (rand_matrix < mask_prob) & (x_0 != model.pad_token_id)
                x_t = x_0.clone()
                x_t[is_masked] = model.mask_token_id

                logits = model(x_t, prompt_ids, t)
                masked_logits = logits[is_masked]
                masked_targets = x_0[is_masked]

                if masked_targets.numel() > 0:
                    batch_val_loss = F.cross_entropy(masked_logits, masked_targets).item()
                else:
                    batch_val_loss = 0.0

                val_total_loss += batch_val_loss
                val_steps += 1

        val_loss = val_total_loss / max(1, val_steps)

        print(f"\n--- Zakończono Epokę {epoch+1} | Średni błąd: {avg_loss:.4f} ---")
        print(f"Średni loss w epoce {epoch+1}: {avg_loss:.6f}")
        print(f"Walidacyjny loss w epoce {epoch+1}: {val_loss:.6f}")

        if experiment is not None:
            experiment.log_metric("epoch_loss", avg_loss, step=epoch + 1)
            experiment.log_metric("epoch_avg_loss", avg_loss, step=epoch + 1)
            experiment.log_metric("val_loss", val_loss, step=epoch + 1)
            experiment.log_metric("lr", optimizer.param_groups[0]["lr"], step=epoch + 1)

        if scheduler is not None:
            previous_lr = optimizer.param_groups[0]["lr"]
            scheduler.step(val_loss)
            new_lr = optimizer.param_groups[0]["lr"]
            if new_lr < previous_lr:
                print(f"ReduceLROnPlateau: lr {previous_lr:.6g} -> {new_lr:.6g}")

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            epochs_without_improvement = 0

            print(f"[BEST] Nowy najlepszy val_loss: {val_loss:.6f}")

            checkpoint = {
                "epoch": epoch + 1,
                "val_loss": val_loss,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
            }
            checkpoint_path = checkpoint_dir / "diffcoder_best.pt"

            # Save both a canonical name and an epoched copy so we can keep a small history locally
            epoch_num = epoch + 1
            checkpoint_epoch_path = checkpoint_dir / f"diffcoder_best_epoch_{epoch_num}.pt"
            try:
                torch.save(checkpoint, checkpoint_epoch_path)
                torch.save(checkpoint, checkpoint_path)
            except Exception as e:
                print(f"Błąd zapisu checkpointu: {e}")
            print(f"Nowy najlepszy checkpoint lokalny zapisany: {checkpoint_path} (epoka {epoch_num})")

            # Immediately prune local epoched checkpoints to free disk space
            try:
                prune_local_checkpoints(checkpoint_dir, keep_last=3)
            except Exception:
                pass

            if experiment is not None:
                print("Kolejkuję model do wysyłki na Comet ML (asynchronicznie)...")
                # ensure uploader queue exists
                global _comet_uploader_queue
                if _comet_uploader_queue is None:
                    _comet_uploader_queue = _queue.Queue(maxsize=3)

                # If queue is full, drop the oldest task to make room
                try:
                    if _comet_uploader_queue.full():
                        try:
                            dropped = _comet_uploader_queue.get_nowait()
                            print(f"[COMET-UPLOADER] Kolejka pełna, usuwam najstarsze zadanie: {dropped[1]}")
                        except Exception:
                            pass
                    _comet_uploader_queue.put_nowait((checkpoint_path, epoch_num))
                except Exception as e:
                    print(f"[COMET-UPLOADER] Nie udało się dodać zadania do kolejki: {e}")

                print("Zadanie wysyłki dodane do kolejki.")

            # delete previous canonical best if different
            if best_checkpoint_path is not None and best_checkpoint_path != checkpoint_path:
                try:
                    best_checkpoint_path.unlink()
                    print(f"Usunięto poprzedni najlepszy checkpoint z dysku: {best_checkpoint_path}")
                except Exception as e:
                    print(f"Ostrzeżenie: Nie udało się usunąć poprzedniego checkpointu: {e}")

            best_checkpoint_path = checkpoint_path
        else:
            epochs_without_improvement += 1
            print(
                f"Brak poprawy val loss przez {epochs_without_improvement} epok(e). "
                f"Najlepszy val loss: {best_val_loss:.6f}"
            )

        release_training_memory()

        if sample_pairs:
            log_generated_samples(
                model,
                tokenizer,
                sample_pairs,
                device,
                epoch + 1,
                experiment=experiment,
            )

        if epochs_without_improvement >= early_stopping_patience:
            print(
                f"Early stopping: brak poprawy przez {early_stopping_patience} epok. "
                f"Kończę trening na epoce {epoch+1}."
            )
            break


if __name__ == "__main__":
    load_dotenv()
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Rozpoczynam trening na: {DEVICE}")
    print("Inicjalizuję konfigurację treningu i przygotowuję dane...")

    if DEVICE == "cuda":
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True
        torch.set_float32_matmul_precision("high")
    
    MAX_PROMPT_LEN = 96
    MAX_CODE_LEN = 512
    BATCH_SIZE = 4
    ACCUMULATION_STEPS = 8
    NUM_WORKERS = 3
    EPOCHS = 500
    VAL_SPLIT = 0.1
    EARLY_STOPPING_PATIENCE = 50
    HIDDEN_DIM = 512
    NUM_BLOCKS = 5
    DATASET_FRACTION = float(os.getenv("DATASET_FRACTION", "1.0")) # size of dataset
    BASE_LR = 1e-4
    RESUME_FROM_CHECKPOINT = False # True - restart from checkpoint
    RESUME_CHECKPOINT_NAME = "diffcoder_best.pt" # name of model in folder checkpoint
    LR_PLATEAU_PATIENCE = 5
    LR_PLATEAU_FACTOR = 0.5
    LR_MIN = 1e-5

    tokenizer = CodeTokenizer()

    comet_api_key = os.getenv("COMET_API_KEY")
    comet_project_name = os.getenv("COMET_PROJECT_NAME")
    comet_workspace = os.getenv("COMET_WORKSPACE")

    experiment = None
    if Experiment is not None and comet_api_key and comet_project_name:
        print("Comet ML: aktywuję eksperyment i logowanie metryk.")
        experiment = Experiment(
            api_key=comet_api_key,
            project_name=comet_project_name,
            workspace=comet_workspace,
            auto_output_logging="simple",
        )
        experiment.log_parameters({
            "max_prompt_len": MAX_PROMPT_LEN,
            "max_code_len": MAX_CODE_LEN,
            "batch_size": BATCH_SIZE,
            "epochs": EPOCHS,
            "val_split": VAL_SPLIT,
            "early_stopping_patience": EARLY_STOPPING_PATIENCE,
            "hidden_dim": HIDDEN_DIM,
            "num_blocks": NUM_BLOCKS,
            "dataset_fraction": DATASET_FRACTION,
        })
        # start background uploader thread (non-blocking uploads)
        try:
            _comet_uploader_queue = _queue.Queue(maxsize=3)
            _comet_uploader_stop_event = threading.Event()
            _comet_uploader_thread = threading.Thread(
                target=_comet_uploader_worker,
                args=(experiment, _comet_uploader_queue, _comet_uploader_stop_event, 3),
                daemon=True,
            )
            _comet_uploader_thread.start()
            print("[COMET-UPLOADER] Wątek uploader-a uruchomiony.")
        except Exception as e:
            print(f"[COMET-UPLOADER] Nie udało się uruchomić uploader-a: {e}")
    
    model = LocalConvDiffCoder(
        vocab_size=tokenizer.vocab_size,
        mask_token_id=tokenizer.mask_token_id,
        pad_token_id=tokenizer.pad_token_id,
        hidden_dim=HIDDEN_DIM,
        num_blocks=NUM_BLOCKS,
        max_seq_len=MAX_PROMPT_LEN + MAX_CODE_LEN
    ).to(DEVICE)

    repo_root = Path(__file__).resolve().parents[1]
    checkpoint_dir = repo_root / "checkpoints"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    dataset_path = repo_root / "data" / "dataset.csv"
    dataset = CodeInstructionDataset(
        str(dataset_path),
        tokenizer,
        max_prompt_len=MAX_PROMPT_LEN,
        max_code_len=MAX_CODE_LEN,
        dataset_fraction=DATASET_FRACTION,
    )
    print(f"Zbiór danych załadowany: {len(dataset)} próbek")
    if len(dataset) < 2:
        raise ValueError("Dataset musi mieć co najmniej 2 próbki, aby wykonać split train/validation.")

    val_size = max(1, int(len(dataset) * VAL_SPLIT))
    train_size = len(dataset) - val_size
    if train_size < 1:
        train_size = 1
        val_size = len(dataset) - 1

    split_generator = torch.Generator().manual_seed(42)
    train_dataset, val_dataset = random_split(
        dataset,
        [train_size, val_size],
        generator=split_generator,
    )

    print(
        f"Podział danych: train={len(train_dataset)} próbek, val={len(val_dataset)} próbek "
        f"({VAL_SPLIT * 100:.1f}% walidacji)"
    )
    print(f"Checkpointy będą zapisywane do: {checkpoint_dir}")

    collate_fn = partial(
        collate_batch,
        pad_id=tokenizer.pad_token_id,
        max_prompt_len=MAX_PROMPT_LEN,
        max_code_len=MAX_CODE_LEN,
    )
    train_dataloader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=DEVICE == "cuda",
        persistent_workers=NUM_WORKERS > 0,
        collate_fn=collate_fn,
    )
    val_dataloader = DataLoader(
        val_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=DEVICE == "cuda",
        persistent_workers=NUM_WORKERS > 0,
        collate_fn=collate_fn,
    )
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=BASE_LR, weight_decay=0.01)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer,
        mode="min",
        factor=LR_PLATEAU_FACTOR,
        patience=LR_PLATEAU_PATIENCE,
        min_lr=LR_MIN,
    )

    def resolve_best_checkpoint(path):
        candidates = list(path.glob("diffcoder_best_epoch_*.pt"))
        if not candidates:
            return None

        def extract_epoch(p):
            try:
                return int(p.stem.split("_")[-1])
            except ValueError:
                return -1

        return max(candidates, key=extract_epoch)

    start_epoch = 0
    best_val_loss = None
    best_checkpoint_path = None
    if RESUME_FROM_CHECKPOINT:
        resume_path = None
        if RESUME_CHECKPOINT_NAME:
            resume_path = checkpoint_dir / RESUME_CHECKPOINT_NAME
        else:
            resume_path = resolve_best_checkpoint(checkpoint_dir)
        if resume_path is not None and resume_path.exists():
            checkpoint = torch.load(resume_path, map_location=DEVICE)
            model.load_state_dict(checkpoint["model_state_dict"])
            optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
            # for group in optimizer.param_groups:
            #     group["lr"] = BASE_LR
            start_epoch = int(checkpoint.get("epoch", 0))
            best_val_loss = float(checkpoint.get("val_loss", "inf"))
            best_checkpoint_path = resume_path
            print(
                f"Wznawiam trening z checkpointu: {resume_path} | "
                f"epoch={start_epoch} | best_val_loss={best_val_loss:.6f} | lr={BASE_LR}"
            )
        else:
            print("Nie znaleziono checkpointu do wznowienia. Start od zera.")

    sample_pairs = []
    if len(dataset) > 0:
        rng = random.Random(42)
        sample_indices = rng.sample(range(len(dataset)), min(3, len(dataset)))
        for idx in sample_indices:
            row = dataset.df.iloc[idx]
            sample_pairs.append(
                {
                    "instruction": str(row["instruction"]),
                    "code": str(row["code"]),
                }
            )

    train_diffcoder(
        model,
        train_dataloader,
        val_dataloader,
        optimizer,
        scheduler,
        EPOCHS,
        ACCUMULATION_STEPS,
        EARLY_STOPPING_PATIENCE,
        DEVICE,
        tokenizer,
        sample_pairs,
        checkpoint_dir,
        experiment,
        start_epoch=start_epoch,
        best_val_loss=best_val_loss,
        best_checkpoint_path=best_checkpoint_path,
    )

    if experiment is not None:
        print("Oczekiwanie na zakończenie zadań uploadu do Comet...")
        try:
            if _comet_uploader_queue is not None:
                _comet_uploader_queue.join()
        except Exception:
            pass
        try:
            if _comet_uploader_stop_event is not None:
                _comet_uploader_stop_event.set()
            if _comet_uploader_thread is not None:
                _comet_uploader_thread.join(timeout=10)
        except Exception:
            pass
        experiment.end()