from functools import partial
from pathlib import Path
import os
import random
import ast as _ast
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv

from diffusion.model import LocalConvDiffCoder
from tokenizer import CodeTokenizer 
from diffusion.loss import CalculateLoss

try:
    from comet_ml import Experiment
except Exception:
    Experiment = None


# number of initial epochs to keep mask range fixed at 30-50%
# will be set from env in __main__ (default 10)
INITIAL_FIXED_EPOCHS = 20


def get_epoch_mask_bounds(epoch_number, total_epochs):
    if total_epochs <= 1:
        return 0.30, 1.0

    if INITIAL_FIXED_EPOCHS is not None and epoch_number <= INITIAL_FIXED_EPOCHS:
        return 0.30, 0.50

    warmup_end = min(100, total_epochs)
    full_end = min(250, total_epochs)

    if epoch_number <= warmup_end:
        lower_start = 0.10
        lower_end = 0.20 if warmup_end > 1 else 0.30
        upper_start = 0.30
        upper_end = 0.60 if warmup_end > 1 else 1.0
        progress = (epoch_number - 1) / max(1, warmup_end - 1)
        lower_bound = lower_start + (lower_end - lower_start) * progress
        upper_bound = upper_start + (upper_end - upper_start) * progress
        return lower_bound, upper_bound

    if epoch_number <= full_end:
        lower_start = 0.20
        lower_end = 0.30
        upper_start = 0.60
        upper_end = 1.00
        progress = (epoch_number - warmup_end) / max(1, full_end - warmup_end)
        lower_bound = lower_start + (lower_end - lower_start) * progress
        upper_bound = upper_start + (upper_end - upper_start) * progress
        return lower_bound, upper_bound

    return 0.30, 1.0


def sample_epoch_mask_prob(batch_size, device, epoch_number, total_epochs):
    lower_bound, upper_bound = get_epoch_mask_bounds(epoch_number, total_epochs)
    return lower_bound + torch.rand(batch_size, device=device) * (upper_bound - lower_bound)


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
        # build simple AST node-type vocabulary across dataset (fast heuristic)
        self.node_vocab = {}
        for code in self.df['code'].astype(str):
            try:
                tree = _ast.parse(code)
                for n in _ast.walk(tree):
                    t = type(n).__name__
                    if t not in self.node_vocab:
                        self.node_vocab[t] = len(self.node_vocab)
            except Exception:
                continue
        self.ast_dim = len(self.node_vocab)

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
        # extract simple AST bag-of-node-types vector
        try:
            tree = _ast.parse(row['code'])
            counts = [0] * self.ast_dim
            for n in _ast.walk(tree):
                t = type(n).__name__
                idx_t = self.node_vocab.get(t)
                if idx_t is not None:
                    counts[idx_t] += 1
            ast_vec = torch.tensor(counts, dtype=torch.float)
        except Exception:
            ast_vec = torch.zeros(self.ast_dim, dtype=torch.float)

        return {
            'prompt_ids': prompt_ids,
            'code_ids': code_ids,
            'ast_vec': ast_vec,
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

    result = {
        'prompt_ids': torch.stack(prompt_tensors, dim=0),
        'code_ids': torch.stack(code_tensors, dim=0)
    }

    # include ast vectors if present
    if 'ast_vec' in batch[0]:
        ast_tensors = [item['ast_vec'] for item in batch]
        result['ast_vec'] = torch.stack(ast_tensors, dim=0)

    return result


def log_generated_samples(model, tokenizer, samples, device, epoch, steps=50, experiment=None, checkpoint_dir=None, total_epochs=None):
    """Loguje próbki: instrukcja, ground-truth, masked ground-truth, predicted (forward on masked), generated (full infer).
    Nie zapisuje już CSV — tylko loguje do Comet (table/text) lub stdout.
    """
    model.eval()
    table_rows = []

    for idx, sample in enumerate(samples):
        prompt = sample["instruction"]
        target_code = sample["code"]
        prompt_ids = torch.tensor(tokenizer.encode_instruction(prompt), dtype=torch.long).to(device)
        if prompt_ids.dim() == 1:
            prompt_ids = prompt_ids.unsqueeze(0)

        masked_text = ""
        predicted_text = ""
        gen_text = ""

        # compute masked ground truth and model's prediction on that masked input
        try:
            code_ids_raw = tokenizer.encode_code(target_code)
            x_0 = torch.tensor([code_ids_raw], dtype=torch.long, device=device)
            if total_epochs is None:
                lower_bound, upper_bound = 0.30, 1.0
            else:
                lower_bound, upper_bound = get_epoch_mask_bounds(epoch, total_epochs)
            mask_prob = lower_bound + torch.rand(1, device=device) * (upper_bound - lower_bound)
            rand_matrix = torch.rand(1, x_0.size(1), device=device)
            is_masked = (rand_matrix < mask_prob) & (x_0 != tokenizer.pad_token_id)
            x_masked = x_0.clone()
            x_masked[is_masked] = tokenizer.mask_token_id
            # keep special tokens (mask) visible when decoding masked ground truth
            masked_text = tokenizer.decode(x_masked[0].tolist(), skip_special_tokens=False)

            with torch.no_grad():
                logits = model(x_masked, prompt_ids, mask_prob.view(-1))
                pred_ids = logits.argmax(dim=-1)
                # merge predictions into masked input: replace mask tokens with model preds
                try:
                    mask_id = tokenizer.mask_token_id
                    x_masked_cpu = x_masked[0].cpu().tolist()
                    pred_cpu = pred_ids[0].cpu().tolist()
                    merged = []
                    pred_idx = 0
                    for tok in x_masked_cpu:
                        if tok == mask_id:
                            # take next prediction for this position
                            merged.append(pred_cpu[pred_idx])
                        else:
                            merged.append(tok)
                        pred_idx += 1
                    # keep special tokens visible to inspect masks/preds
                    predicted_text = tokenizer.decode(merged, skip_special_tokens=False)
                except Exception:
                    predicted_text = tokenizer.decode(pred_ids[0].tolist())
        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            masked_text = f"<ERROR: {type(e).__name__}: {e}>\n{tb}"
            predicted_text = masked_text

        # also run full generation (separate inference path)
        try:
            with torch.no_grad():
                gen_ids = model.generate(
                    prompt_ids,
                    steps=steps,
                    device=device,
                    eos_token_id=tokenizer.eos_token_id,
                )
            gen_text = tokenizer.decode(gen_ids[0].tolist())
        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            gen_text = f"<ERROR: {type(e).__name__}: {e}>\n{tb}"

        # log to Comet or stdout
        if experiment is not None:
            experiment.log_text(
                "Epoch "
                f"{epoch} | sample {idx}\nPROMPT:\n{prompt}"
                f"\n\nGROUND_TRUTH:\n{target_code}"
                f"\n\nMASKED_GROUND_TRUTH:\n{masked_text}"
                f"\n\nPREDICTED_THIS_ITERATION:\n{predicted_text}"
                f"\n\nGENERATED:\n{gen_text}",
                step=epoch,
            )
            table_rows.append(
                {
                    "epoch": epoch,
                    "sample": idx,
                    "prompt": prompt,
                    "ground_truth": target_code,
                    "masked_ground_truth": masked_text,
                    "predicted_this_iteration": predicted_text,
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
            print("MASKED_GROUND_TRUTH:")
            print(masked_text)
            print("PREDICTED_THIS_ITERATION:")
            print(predicted_text)
            print("GENERATED:")
            print(gen_text)

    if experiment is not None and table_rows:
        experiment.log_table("generated_samples", table_rows, step=epoch)

    model.train()


def cleanup_checkpoint_dir(checkpoint_dir, keep_path=None):
    """Keep only the selected checkpoint file in checkpoints/.

    Removes all diffcoder_best*.pt files except keep_path.
    """
    for candidate in checkpoint_dir.glob("diffcoder_best*.pt"):
        if keep_path is not None and candidate.resolve() == keep_path.resolve():
            continue
        try:
            candidate.unlink()
            print(f"Usunięto checkpoint: {candidate}")
        except Exception as e:
            print(f"Ostrzeżenie: nie udało się usunąć checkpointu {candidate}: {e}")


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
    epochs_without_improvement=0,
    best_checkpoint_path=None,
    total_epochs=None,
):
    use_amp = device == "cuda"
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp)
    if best_val_loss is None:
        best_val_loss = float("inf")
    # total epochs used to compute epoch-dependent masking schedule
    effective_total_epochs = total_epochs or epochs
    latest_checkpoint_path = checkpoint_dir / "diffcoder_latest.pt"

    # training bookkeeping
    epochs_without_improvement = 0

    # combined loss (classification + dtw) used by this training loop
    loss_fn = CalculateLoss(
        gamma=1.0,
        ce_weight=1.0,
        dtw_weight=0.1,
        embedding_matrix=getattr(model, 'embedding', None).weight if hasattr(model, 'embedding') else None,
    ).to(device)
    
    for epoch in range(start_epoch, epochs):
        model.train()
        total_loss = 0
        epoch_number = epoch + 1
        current_mask_lower_bound, current_mask_upper_bound = get_epoch_mask_bounds(epoch_number, effective_total_epochs)
        print(
            f"Epoka {epoch_number}/{effective_total_epochs} | "
            f"aktualne maskowanie: {current_mask_lower_bound * 100:.1f}% - {current_mask_upper_bound * 100:.1f}%"
        )
        progress_bar = tqdm(
            enumerate(train_dataloader),
            total=len(train_dataloader),
            desc=f"Epoka {epoch_number}/{effective_total_epochs}",
        )
        optimizer.zero_grad()
            
        for batch_idx, batch in progress_bar:
            x_0 = batch['code_ids'].to(device)
            prompt_ids = batch['prompt_ids'].to(device)
                
            batch_size, seq_len = x_0.shape

            mask_prob = sample_epoch_mask_prob(batch_size, device, epoch_number, effective_total_epochs)
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
                # prepare ast embeddings projection if available
                ast_embeddings = None
                if 'ast_vec' in batch and batch.get('ast_vec') is not None:
                    ast_vec = batch.get('ast_vec').to(device)
                    embed_mat = loss_fn.embedding_matrix if hasattr(loss_fn, 'embedding_matrix') else None
                    if embed_mat is not None:
                        try:
                            # ensure embed_mat on same device
                            embed_mat = embed_mat.to(device)
                        except Exception:
                            pass
                    if embed_mat is not None and embed_mat.size(0) >= ast_vec.size(1):
                        W = embed_mat[:ast_vec.size(1), :]
                    elif embed_mat is not None:
                        W = embed_mat.mean(dim=0, keepdim=True).repeat(ast_vec.size(1), 1)
                    else:
                        W = None

                    if W is not None:
                        ast_proj = ast_vec @ W
                        ast_embeddings = ast_proj.unsqueeze(1)

                loss, ce_loss, dtw_loss = loss_fn(
                    full_logits=logits, 
                    masked_logits=masked_logits, 
                    masked_targets=masked_targets,
                    ast_embeddings=ast_embeddings,
                )
                            
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

                mask_prob = sample_epoch_mask_prob(batch_size, device, epoch_number, effective_total_epochs)
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
                    # prepare ast embeddings for validation batch (same projection as training)
                    ast_embeddings = None
                    if val_batch.get('ast_vec') is not None:
                        ast_vec = val_batch.get('ast_vec').to(device)
                        embed_mat = loss_fn.embedding_matrix if hasattr(loss_fn, 'embedding_matrix') else None
                        if embed_mat is not None:
                            try:
                                embed_mat = embed_mat.to(device)
                            except Exception:
                                pass
                        if embed_mat is not None and embed_mat.size(0) >= ast_vec.size(1):
                            W = embed_mat[:ast_vec.size(1), :]
                        elif embed_mat is not None:
                            W = embed_mat.mean(dim=0, keepdim=True).repeat(ast_vec.size(1), 1)
                        else:
                            W = None

                        if W is not None:
                            ast_proj = ast_vec @ W
                            ast_embeddings = ast_proj.unsqueeze(1)

                    val_loss_tensor, _, _ = loss_fn(
                        full_logits=logits,
                        masked_logits=masked_logits,
                        masked_targets=masked_targets,
                        ast_embeddings=ast_embeddings,
                    )
                    batch_val_loss = val_loss_tensor.item()
                else:
                    batch_val_loss = 0.0

                val_total_loss += batch_val_loss
                val_steps += 1

        val_loss = val_total_loss / max(1, val_steps)

        print(f"\n--- Zakończono Epokę {epoch+1} | Średni błąd: {avg_loss:.4f} ---")
        print(f"Średni loss w epoce {epoch+1}: {avg_loss:.6f}")
        print(f"Walidacyjny loss w epoce {epoch+1}: {val_loss:.6f}")

        previous_lr = optimizer.param_groups[0]["lr"]
        if scheduler is not None:
            scheduler.step(val_loss)
        current_lr = optimizer.param_groups[0]["lr"]

        if experiment is not None:
            experiment.log_metric("epoch_loss", avg_loss, step=epoch + 1)
            experiment.log_metric("epoch_avg_loss", avg_loss, step=epoch + 1)
            experiment.log_metric("val_loss", val_loss, step=epoch + 1)
            experiment.log_metric("lr", current_lr, step=epoch + 1)

        if current_lr < previous_lr:
            print(f"ReduceLROnPlateau obniżył lr: {previous_lr:.8f} -> {current_lr:.8f}")

        improved = val_loss < best_val_loss
        if improved:
            best_val_loss = val_loss
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1

        checkpoint = {
            "epoch": epoch + 1,
            "total_epochs": effective_total_epochs,
            "mask_lower_bound": current_mask_lower_bound,
            "mask_upper_bound": current_mask_upper_bound,
            "val_loss": val_loss,
            "best_val_loss": best_val_loss,
            "epochs_without_improvement": epochs_without_improvement,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "scheduler_state_dict": None if scheduler is None else scheduler.state_dict(),
        }
        torch.save(checkpoint, latest_checkpoint_path)
        print(
            f"Zapisano checkpoint bieżący: {latest_checkpoint_path} | "
            f"lr={current_lr:.8f}"
        )

        if improved:
            checkpoint_path = checkpoint_dir / "diffcoder_best.pt"
            torch.save(checkpoint, checkpoint_path)
            cleanup_checkpoint_dir(checkpoint_dir, keep_path=checkpoint_path)
            print(f"Nowy najlepszy checkpoint lokalny zapisany: {checkpoint_path}")

            if experiment is not None:
                print("Kolejkuję model do wysyłki na Comet ML...")
                experiment.log_other("best_model_epoch", epoch + 1)
                experiment.log_other("best_model_val_loss", val_loss)
                experiment.log_model(
                    name="diffcoder_best",
                    file_or_folder=str(checkpoint_path),
                    overwrite=True,
                )

            best_checkpoint_path = checkpoint_path
        else:
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
                epoch_number,
                experiment=experiment,
                checkpoint_dir=checkpoint_dir,
                total_epochs=effective_total_epochs,
            )

        if epochs_without_improvement >= early_stopping_patience:
            print(
                f"Early stopping: brak poprawy przez {early_stopping_patience} epok. "
                f"Kończę trening na epoce {epoch+1}."
            )
            break


if __name__ == "__main__":
    load_dotenv()
    # configure INITIAL_FIXED_EPOCHS after loading dotenv so .env is respected
    INITIAL_FIXED_EPOCHS = int(os.getenv("INITIAL_FIXED_EPOCHS", "10"))
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
    EARLY_STOPPING_PATIENCE = 50
    HIDDEN_DIM = 512
    NUM_BLOCKS = 6
    DILATION_FACTOR = int(os.getenv("DILATION_FACTOR", "2"))
    DATASET_FRACTION = float(os.getenv("DATASET_FRACTION", "1.0")) # size of dataset
    BASE_LR = 5e-5
    LR_SCHEDULER_FACTOR = 0.5
    LR_SCHEDULER_PATIENCE = 8
    LR_SCHEDULER_MIN_LR = 1e-6
    LR_SCHEDULER_THRESHOLD = 1e-4
    LR_SCHEDULER_COOLDOWN = 2
    RESUME_FROM_CHECKPOINT = True
    RESUME_CHECKPOINT_NAME = "diffcoder_best.pt"

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
            "base_lr": BASE_LR,
            "lr_scheduler_factor": LR_SCHEDULER_FACTOR,
            "lr_scheduler_patience": LR_SCHEDULER_PATIENCE,
            "lr_scheduler_min_lr": LR_SCHEDULER_MIN_LR,
            "lr_scheduler_threshold": LR_SCHEDULER_THRESHOLD,
            "lr_scheduler_cooldown": LR_SCHEDULER_COOLDOWN,
        })
    
    model = LocalConvDiffCoder(
        vocab_size=tokenizer.vocab_size,
        mask_token_id=tokenizer.mask_token_id,
        pad_token_id=tokenizer.pad_token_id,
        hidden_dim=HIDDEN_DIM,
        num_blocks=NUM_BLOCKS,
        max_seq_len=MAX_PROMPT_LEN + MAX_CODE_LEN,
        dilation_factor=DILATION_FACTOR,
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
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=BASE_LR, weight_decay=0.01)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer,
        mode="min",
        factor=LR_SCHEDULER_FACTOR,
        patience=LR_SCHEDULER_PATIENCE,
        threshold=LR_SCHEDULER_THRESHOLD,
        cooldown=LR_SCHEDULER_COOLDOWN,
        min_lr=LR_SCHEDULER_MIN_LR,
    )

    def resolve_resume_checkpoint(path):
        latest_checkpoint = path / "diffcoder_latest.pt"
        if latest_checkpoint.exists():
            return latest_checkpoint

        best_checkpoint = path / "diffcoder_best.pt"
        if best_checkpoint.exists():
            return best_checkpoint

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
    training_total_epochs = EPOCHS
    epochs_without_improvement = 0
    if RESUME_FROM_CHECKPOINT:
        resume_path = None
        if RESUME_CHECKPOINT_NAME:
            resume_path = checkpoint_dir / RESUME_CHECKPOINT_NAME
        else:
            resume_path = resolve_resume_checkpoint(checkpoint_dir)
        if resume_path is not None and resume_path.exists():
            checkpoint = torch.load(resume_path, map_location=DEVICE)
            model.load_state_dict(checkpoint["model_state_dict"])
            optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
            scheduler_state_dict = checkpoint.get("scheduler_state_dict")
            if scheduler_state_dict is not None:
                scheduler.load_state_dict(scheduler_state_dict)
            start_epoch = int(checkpoint.get("epoch", 0))
            training_total_epochs = int(checkpoint.get("total_epochs", EPOCHS))
            best_val_loss = float(checkpoint.get("best_val_loss", checkpoint.get("val_loss", "inf")))
            epochs_without_improvement = int(checkpoint.get("epochs_without_improvement", 0))
            best_checkpoint_path = resume_path
            cleanup_checkpoint_dir(checkpoint_dir, keep_path=best_checkpoint_path)
            print(
                f"Wznawiam trening z checkpointu: {resume_path} | "
                f"epoch={start_epoch} | total_epochs={training_total_epochs} | "
                f"best_val_loss={best_val_loss:.6f} | lr={optimizer.param_groups[0]['lr']:.8f}"
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
        model=model,
        train_dataloader=train_dataloader,
        val_dataloader=val_dataloader,
        optimizer=optimizer,
        scheduler=scheduler,
        epochs=EPOCHS,
        accumulation_steps=ACCUMULATION_STEPS,
        early_stopping_patience=EARLY_STOPPING_PATIENCE,
        device=DEVICE,
        tokenizer=tokenizer,
        sample_pairs=sample_pairs,
        checkpoint_dir=checkpoint_dir,
        experiment=experiment,
        start_epoch=start_epoch,
        best_val_loss=best_val_loss,
        epochs_without_improvement=epochs_without_improvement,
        best_checkpoint_path=best_checkpoint_path,
        total_epochs=training_total_epochs,
    )

    if experiment is not None:
        experiment.end()
