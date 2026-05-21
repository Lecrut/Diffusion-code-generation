from functools import partial
from pathlib import Path
import os
import random
import math
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
    epochs,
    accumulation_steps,
    early_stopping_patience,
    device,
    tokenizer,
    sample_pairs,
    checkpoint_dir,
    experiment=None,
):
    use_amp = device == "cuda"
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp)
    best_val_loss = float("inf")
    best_checkpoint_path = None
    epochs_without_improvement = 0
    
    for epoch in range(epochs):
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

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            epochs_without_improvement = 0

            checkpoint = {
                "epoch": epoch + 1,
                "val_loss": val_loss,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
            }
            checkpoint_path = checkpoint_dir / f"diffcoder_best_epoch_{epoch+1}.pt"
            torch.save(checkpoint, checkpoint_path)
            print(f"Nowy najlepszy checkpoint lokalny zapisany: {checkpoint_path}")

            if experiment is not None:
                print("Kolejkuję model do wysyłki na Comet ML...")
                experiment.log_model(
                    name="diffcoder",
                    file_or_folder=str(checkpoint_path),
                    overwrite=True,
                )

            if best_checkpoint_path is not None and best_checkpoint_path.exists():
                try:
                    os.remove(best_checkpoint_path)
                    print(f"Usunięto stary checkpoint z dysku: {best_checkpoint_path}")
                except Exception as e:
                    print(f"Ostrzeżenie: Nie udało się usunąć lokalnego checkpointu: {e}")

            best_checkpoint_path = checkpoint_path
        else:
            epochs_without_improvement += 1
            print(
                f"Brak poprawy val loss przez {epochs_without_improvement} epok(e). "
                f"Najlepszy val loss: {best_val_loss:.6f}"
            )

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
    VAL_SPLIT = 0.05
    EARLY_STOPPING_PATIENCE = 20
    HIDDEN_DIM = 256
    NUM_BLOCKS = 4
    DATASET_FRACTION = float(os.getenv("DATASET_FRACTION", "1.0")) # size of dataset

    tokenizer = CodeTokenizer()

    comet_api_key = os.getenv("COMET_API_KEY")
    comet_project_name = os.getenv("COMET_PROJECT_NAME")
    comet_workspace = os.getenv("COMET_WORKSPACE")

    experiment = None
    if Experiment is not None and comet_api_key and comet_project_name:
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
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.01)

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
        EPOCHS,
        ACCUMULATION_STEPS,
        EARLY_STOPPING_PATIENCE,
        DEVICE,
        tokenizer,
        sample_pairs,
        checkpoint_dir,
        experiment,
    )

    if experiment is not None:
        experiment.end()