from datetime import datetime
from functools import partial
from pathlib import Path
import os
import random
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv

from diffusion.model import ContinuousDiffusionUNet
from tokenizer import CodeTokenizer

try:
    from comet_ml import Experiment
except Exception:
    Experiment = None


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
        self.df = self.df[["instruction", "code"]].dropna()
        if not (0.0 < dataset_fraction <= 1.0):
            raise ValueError("dataset_fraction must be in (0.0, 1.0].")
        if dataset_fraction < 1.0:
            keep = max(1, int(len(self.df) * dataset_fraction))
            self.df = self.df.sample(n=keep, random_state=seed).reset_index(drop=True)
        self.tokenizer    = tokenizer
        self.max_prompt_len = max_prompt_len
        self.max_code_len   = max_code_len
        self.pad_id         = self.tokenizer.pad_token_id

    def __len__(self):
        return len(self.df)

    def _pad_or_truncate(self, ids, max_len):
        if len(ids) > max_len:
            return ids[:max_len]
        return ids

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        prompt_ids = self._pad_or_truncate(
            self.tokenizer.encode_instruction(row["instruction"]), self.max_prompt_len
        )
        code_ids = self._pad_or_truncate(
            self.tokenizer.encode_code(row["code"]), self.max_code_len
        )
        return {"prompt_ids": prompt_ids, "code_ids": code_ids}


def collate_batch(batch, pad_id, max_prompt_len, max_code_len):
    prompt_max = min(max(len(item["prompt_ids"]) for item in batch), max_prompt_len)
    code_max   = min(max(len(item["code_ids"])   for item in batch), max_code_len)

    prompt_tensors, code_tensors = [], []
    for item in batch:
        p = item["prompt_ids"][:prompt_max]
        c = item["code_ids"][:code_max]
        p = p + [pad_id] * (prompt_max - len(p))
        c = c + [pad_id] * (code_max   - len(c))
        prompt_tensors.append(torch.tensor(p, dtype=torch.long))
        code_tensors.append(torch.tensor(c,   dtype=torch.long))

    return {
        "prompt_ids": torch.stack(prompt_tensors),
        "code_ids":   torch.stack(code_tensors),
    }


def log_generated_samples(model, tokenizer, samples, device, epoch, steps=50, experiment=None):
    model.eval()
    table_rows = []
    for idx, sample in enumerate(samples):
        prompt     = sample["instruction"]
        target_code = sample["code"]
        prompt_ids  = torch.tensor(
            tokenizer.encode_instruction(prompt), dtype=torch.long
        ).to(device)

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
                f"Epoch {epoch} | sample {idx}\nPROMPT:\n{prompt}"
                f"\n\nGROUND_TRUTH:\n{target_code}"
                f"\n\nGENERATED:\n{gen_text}",
                step=epoch,
            )
            table_rows.append({
                "epoch": epoch, "sample": idx,
                "prompt": prompt, "ground_truth": target_code, "generated": gen_text,
            })
        else:
            print("-" * 80)
            print(f"Epoch {epoch} | sample {idx}")
            print("PROMPT:");      print(prompt)
            print("GROUND_TRUTH:"); print(target_code)
            print("GENERATED:");   print(gen_text)

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
    scaler  = torch.amp.GradScaler("cuda", enabled=use_amp)
    if best_val_loss is None:
        best_val_loss = float("inf")
    epochs_without_improvement = 0

    for epoch in range(start_epoch, epochs):
        model.train()
        total_loss = 0.0
        optimizer.zero_grad()
        progress_bar = tqdm(
            enumerate(train_dataloader),
            total=len(train_dataloader),
            desc=f"Epoka {epoch + 1}/{epochs}",
        )

        for batch_idx, batch in progress_bar:
            code_ids   = batch["code_ids"].to(device)
            prompt_ids = batch["prompt_ids"].to(device)


            with torch.amp.autocast("cuda", enabled=use_amp):
                loss = model.compute_loss(code_ids, prompt_ids)

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
            progress_bar.set_postfix({"loss": f"{current_loss:.4f}"})

            if experiment is not None:
                step = epoch * len(train_dataloader) + batch_idx
                experiment.log_metric("train_loss", current_loss, step=step)

        avg_loss = total_loss / len(train_dataloader)
        model.eval()
        val_total_loss = 0.0
        val_steps      = 0
        with torch.no_grad():
            for val_batch in val_dataloader:
                code_ids   = val_batch["code_ids"].to(device)
                prompt_ids = val_batch["prompt_ids"].to(device)

                val_total_loss += model.compute_loss(code_ids, prompt_ids).item()
                val_steps += 1

        val_loss = val_total_loss / max(1, val_steps)

        print(f"\n--- Zakończono Epokę {epoch + 1} ---")
        print(f"Średni train loss: {avg_loss:.6f}")
        print(f"Walidacyjny loss:  {val_loss:.6f}")

        if experiment is not None:
            experiment.log_metric("epoch_avg_loss", avg_loss, step=epoch + 1)
            experiment.log_metric("val_loss",        val_loss, step=epoch + 1)
            experiment.log_metric("lr", optimizer.param_groups[0]["lr"], step=epoch + 1)

        if scheduler is not None:
            previous_lr = optimizer.param_groups[0]["lr"]
            scheduler.step(val_loss)
            new_lr = optimizer.param_groups[0]["lr"]
            if new_lr < previous_lr:
                print(f"ReduceLROnPlateau: lr {previous_lr:.6g} → {new_lr:.6g}")

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            epochs_without_improvement = 0
            checkpoint = {
                "epoch":                epoch + 1,
                "val_loss":             val_loss,
                "model_state_dict":     model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
            }
            checkpoint_path = checkpoint_dir / f"diffcoder_best_epoch_{epoch + 1}.pt"
            torch.save(checkpoint, checkpoint_path)
            print(f"Nowy najlepszy checkpoint: {checkpoint_path}")

            if experiment is not None:
                experiment.log_model("diffcoder", str(checkpoint_path), overwrite=True)

            if best_checkpoint_path is not None and best_checkpoint_path.exists():
                try:
                    os.remove(best_checkpoint_path)
                    print(f"Usunięto stary checkpoint: {best_checkpoint_path}")
                except Exception as e:
                    print(f"Ostrzeżenie: {e}")

            best_checkpoint_path = checkpoint_path
        else:
            epochs_without_improvement += 1
            print(
                f"Brak poprawy przez {epochs_without_improvement} epok(e). "
                f"Najlepszy val loss: {best_val_loss:.6f}"
            )

        if sample_pairs:
            log_generated_samples(
                model, tokenizer, sample_pairs, device, epoch + 1, experiment=experiment
            )

        if epochs_without_improvement >= early_stopping_patience:
            print(
                f"Early stopping po {early_stopping_patience} epokach bez poprawy "
                f"(epoka {epoch + 1})."
            )
            break


if __name__ == "__main__":
    load_dotenv()
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Rozpoczynam trening na: {DEVICE}")

    if DEVICE == "cuda":
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32       = True
        torch.set_float32_matmul_precision("high")

    MAX_PROMPT_LEN          = 96
    MAX_CODE_LEN            = 512
    BATCH_SIZE              = 4
    ACCUMULATION_STEPS      = 8
    NUM_WORKERS             = 3
    EPOCHS                  = 500
    VAL_SPLIT               = 0.1
    EARLY_STOPPING_PATIENCE = 50
    HIDDEN_DIM              = 256
    NUM_DOWN                = 2
    NUM_BOTTLENECK          = 4
    DIFFUSION_T             = 1000
    DATASET_FRACTION        = float(os.getenv("DATASET_FRACTION", "1.0"))
    BASE_LR                 = 1e-4
    RESUME_FROM_CHECKPOINT  = False
    RESUME_CHECKPOINT_NAME  = ""
    LR_PLATEAU_PATIENCE     = 5
    LR_PLATEAU_FACTOR       = 0.5
    LR_MIN                  = 1e-5

    tokenizer = CodeTokenizer()

    comet_api_key      = os.getenv("COMET_API_KEY")
    comet_project_name = os.getenv("COMET_PROJECT_NAME")
    comet_workspace    = os.getenv("COMET_WORKSPACE")
    experiment_name    = str(os.getenv("EXPERIMENT_NAME", "diffusion_training") + datetime.now().strftime("%Y%m%d-%H%M%S"))

    experiment = None
    if Experiment is not None and comet_api_key and comet_project_name:
        experiment = Experiment(
            api_key=comet_api_key,
            project_name=comet_project_name,
            workspace=comet_workspace,
            auto_output_logging="simple",
        )
        experiment.set_name(experiment_name)
        print(f"Experiment name: {experiment_name}")
        experiment.log_parameters({
            "max_prompt_len":          MAX_PROMPT_LEN,
            "max_code_len":            MAX_CODE_LEN,
            "batch_size":              BATCH_SIZE,
            "epochs":                  EPOCHS,
            "val_split":               VAL_SPLIT,
            "early_stopping_patience": EARLY_STOPPING_PATIENCE,
            "hidden_dim":              HIDDEN_DIM,
            "num_down":                NUM_DOWN,
            "num_bottleneck":          NUM_BOTTLENECK,
            "diffusion_T":             DIFFUSION_T,
            "dataset_fraction":        DATASET_FRACTION,
        })

    model = ContinuousDiffusionUNet(
        vocab_size     = tokenizer.vocab_size,
        pad_token_id   = tokenizer.pad_token_id,
        hidden_dim     = HIDDEN_DIM,
        num_down       = NUM_DOWN,
        num_bottleneck = NUM_BOTTLENECK,
        max_seq_len    = MAX_PROMPT_LEN + MAX_CODE_LEN,
        T              = DIFFUSION_T,
    ).to(DEVICE)

    total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Parametry modelu: {total_params:,}")

    repo_root      = Path(__file__).resolve().parents[1]
    checkpoint_dir = repo_root / "checkpoints"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    dataset_path   = repo_root / "data" / "dataset.csv"

    dataset = CodeInstructionDataset(
        str(dataset_path),
        tokenizer,
        max_prompt_len=MAX_PROMPT_LEN,
        max_code_len=MAX_CODE_LEN,
        dataset_fraction=DATASET_FRACTION,
    )
    if len(dataset) < 2:
        raise ValueError("Dataset musi mieć co najmniej 2 próbki.")

    val_size   = max(1, int(len(dataset) * VAL_SPLIT))
    train_size = len(dataset) - val_size
    if train_size < 1:
        train_size, val_size = 1, len(dataset) - 1

    split_generator = torch.Generator().manual_seed(42)
    train_dataset, val_dataset = random_split(
        dataset, [train_size, val_size], generator=split_generator
    )
    print(
        f"Podział danych: train={len(train_dataset)}, val={len(val_dataset)} "
        f"({VAL_SPLIT * 100:.1f}% walidacji)"
    )

    collate_fn = partial(
        collate_batch,
        pad_id=tokenizer.pad_token_id,
        max_prompt_len=MAX_PROMPT_LEN,
        max_code_len=MAX_CODE_LEN,
    )
    train_dataloader = DataLoader(
        train_dataset, batch_size=BATCH_SIZE, shuffle=True,
        num_workers=NUM_WORKERS, pin_memory=DEVICE == "cuda",
        persistent_workers=NUM_WORKERS > 0, collate_fn=collate_fn,
    )
    val_dataloader = DataLoader(
        val_dataset, batch_size=BATCH_SIZE, shuffle=False,
        num_workers=NUM_WORKERS, pin_memory=DEVICE == "cuda",
        persistent_workers=NUM_WORKERS > 0, collate_fn=collate_fn,
    )

    optimizer = torch.optim.AdamW(model.parameters(), lr=BASE_LR, weight_decay=0.01)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode="min", factor=LR_PLATEAU_FACTOR,
        patience=LR_PLATEAU_PATIENCE, min_lr=LR_MIN,
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

    start_epoch        = 0
    best_val_loss      = None
    best_checkpoint_path = None

    if RESUME_FROM_CHECKPOINT:
        resume_path = (
            checkpoint_dir / RESUME_CHECKPOINT_NAME
            if RESUME_CHECKPOINT_NAME
            else resolve_best_checkpoint(checkpoint_dir)
        )
        if resume_path is not None and resume_path.exists():
            ckpt = torch.load(resume_path, map_location=DEVICE)
            model.load_state_dict(ckpt["model_state_dict"])
            optimizer.load_state_dict(ckpt["optimizer_state_dict"])
            for group in optimizer.param_groups:
                group["lr"] = BASE_LR
            start_epoch  = int(ckpt.get("epoch", 0))
            best_val_loss = float(ckpt.get("val_loss", "inf"))
            best_checkpoint_path = resume_path
            print(
                f"Wznawiam z checkpointu: {resume_path} | "
                f"epoch={start_epoch} | best_val_loss={best_val_loss:.6f}"
            )
        else:
            print("Nie znaleziono checkpointu. Start od zera.")

    sample_pairs = []
    if len(dataset) > 0:
        rng = random.Random(42)
        for idx in rng.sample(range(len(dataset)), min(3, len(dataset))):
            row = dataset.df.iloc[idx]
            sample_pairs.append({
                "instruction": str(row["instruction"]),
                "code":        str(row["code"]),
            })

    train_diffcoder(
        model, train_dataloader, val_dataloader, optimizer, scheduler,
        EPOCHS, ACCUMULATION_STEPS, EARLY_STOPPING_PATIENCE, DEVICE,
        tokenizer, sample_pairs, checkpoint_dir, experiment,
        start_epoch=start_epoch,
        best_val_loss=best_val_loss,
        best_checkpoint_path=best_checkpoint_path,
    )

    if experiment is not None:
        experiment.end()