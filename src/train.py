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

from diffusion.checkpoint import adapt_state_dict_to_tokenizer
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
MONITOR_OBJECTIVE_VERSION = "generation_blend_v1"


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


def sample_epoch_mask_prob(batch_size, device, lower_bound, upper_bound):
    return lower_bound + torch.rand(batch_size, device=device) * (upper_bound - lower_bound)


def get_resume_mask_bounds(epoch_number, total_epochs, start_epoch, fixed_epochs):
    if fixed_epochs is not None and fixed_epochs > 0 and epoch_number <= start_epoch + fixed_epochs:
        return 0.30, 0.50
    return get_epoch_mask_bounds(epoch_number, total_epochs)


def parse_bool_env(name, default=False):
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def float_close(left, right, tolerance=1e-9):
    return abs(float(left) - float(right)) <= tolerance


def checkpoint_monitor_config_matches(checkpoint, monitor_mask_bounds, generation_mask_bounds, generation_monitor_weight):
    return (
        checkpoint.get("monitor_objective_version") == MONITOR_OBJECTIVE_VERSION
        and float_close(checkpoint.get("monitor_mask_lower_bound", -1.0), monitor_mask_bounds[0])
        and float_close(checkpoint.get("monitor_mask_upper_bound", -1.0), monitor_mask_bounds[1])
        and float_close(checkpoint.get("generation_mask_lower_bound", -1.0), generation_mask_bounds[0])
        and float_close(checkpoint.get("generation_mask_upper_bound", -1.0), generation_mask_bounds[1])
        and float_close(checkpoint.get("generation_monitor_weight", -1.0), generation_monitor_weight)
    )


def resolve_loss_embedding_matrix(model):
    token_embedding = getattr(model, "token_embedding", None)
    if token_embedding is not None and hasattr(token_embedding, "weight"):
        return token_embedding.weight

    legacy_embedding = getattr(model, "embedding", None)
    if legacy_embedding is not None and hasattr(legacy_embedding, "weight"):
        return legacy_embedding.weight

    return None


def build_ast_embeddings(batch, device, loss_fn):
    if (
        loss_fn.dtw_weight == 0.0
        or loss_fn.embedding_matrix is None
        or "ast_vec" not in batch
        or batch.get("ast_vec") is None
    ):
        return None

    ast_vec = batch.get("ast_vec").to(device)
    embed_mat = loss_fn.embedding_matrix.to(device)

    if embed_mat.size(0) >= ast_vec.size(1):
        projection = embed_mat[:ast_vec.size(1), :]
    else:
        projection = embed_mat.mean(dim=0, keepdim=True).repeat(ast_vec.size(1), 1)

    return (ast_vec @ projection).unsqueeze(1)


def evaluate_diffcoder_loss(model, dataloader, loss_fn, device, mask_bounds, use_amp):
    model.eval()
    lower_bound, upper_bound = mask_bounds
    total_loss = 0.0
    total_ce_loss = 0.0
    total_dtw_loss = 0.0
    total_masked_tokens = 0
    total_candidate_tokens = 0
    steps = 0

    with torch.no_grad():
        for batch in dataloader:
            x_0 = batch["code_ids"].to(device)
            prompt_ids = batch["prompt_ids"].to(device)
            batch_size, seq_len = x_0.shape

            mask_prob = sample_epoch_mask_prob(batch_size, device, lower_bound, upper_bound)
            mask_prob = mask_prob.view(batch_size, 1)
            t = mask_prob.view(-1)
            rand_matrix = torch.rand(batch_size, seq_len, device=device)

            candidate_tokens = x_0 != model.pad_token_id
            is_masked = (rand_matrix < mask_prob) & candidate_tokens
            x_t = x_0.clone()
            x_t[is_masked] = model.mask_token_id

            with torch.amp.autocast("cuda", enabled=use_amp):
                logits = model(x_t, prompt_ids, t)
                masked_logits = logits[is_masked]
                masked_targets = x_0[is_masked]
                ast_embeddings = build_ast_embeddings(batch, device, loss_fn)
                loss, ce_loss, dtw_loss = loss_fn(
                    full_logits=logits,
                    masked_logits=masked_logits,
                    masked_targets=masked_targets,
                    ast_embeddings=ast_embeddings,
                )

            total_loss += loss.item()
            total_ce_loss += ce_loss.item()
            total_dtw_loss += dtw_loss.item()
            total_masked_tokens += int(is_masked.sum().item())
            total_candidate_tokens += int(candidate_tokens.sum().item())
            steps += 1

    return {
        "loss": total_loss / max(1, steps),
        "ce_loss": total_ce_loss / max(1, steps),
        "dtw_loss": total_dtw_loss / max(1, steps),
        "masked_token_ratio": total_masked_tokens / max(1, total_candidate_tokens),
    }


def evaluate_generation_quality(
    model,
    tokenizer,
    samples,
    device,
    steps,
    max_code_len,
    max_prompt_len,
):
    model.eval()
    if not samples:
        return None

    compile_ok = 0
    parse_ok = 0
    eos_count = 0
    nonempty_count = 0
    total_tokens = 0
    total_chars = 0

    with torch.no_grad():
        for sample in samples:
            prompt_ids = tokenizer.encode_instruction(sample["instruction"])[:max_prompt_len]
            prompt_tensor = torch.tensor(prompt_ids, dtype=torch.long, device=device)
            generated_ids = model.generate(
                prompt_tensor,
                steps=steps,
                device=device,
                eos_token_id=tokenizer.eos_token_id,
                max_code_len=max_code_len,
            )[0].detach().cpu().tolist()
            generated_code = tokenizer.decode(generated_ids)

            total_tokens += len(generated_ids)
            total_chars += len(generated_code)
            nonempty_count += int(bool(generated_code.strip()))
            eos_count += int(tokenizer.eos_token_id is not None and tokenizer.eos_token_id in generated_ids)

            try:
                _ast.parse(generated_code)
                parse_ok += 1
            except SyntaxError:
                pass

            try:
                compile(generated_code, "<generated>", "exec")
                compile_ok += 1
            except Exception:
                pass

    sample_count = len(samples)
    return {
        "compile_pass_rate": compile_ok / max(1, sample_count),
        "parse_pass_rate": parse_ok / max(1, sample_count),
        "eos_rate": eos_count / max(1, sample_count),
        "nonempty_rate": nonempty_count / max(1, sample_count),
        "avg_generated_tokens": total_tokens / max(1, sample_count),
        "avg_generated_chars": total_chars / max(1, sample_count),
        "sample_count": sample_count,
    }


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

    def _pad_or_truncate_code(self, ids, max_len):
        if max_len <= 0:
            return []
        if len(ids) <= max_len:
            return ids
        truncated = ids[:max_len]
        eos_id = self.tokenizer.eos_token_id
        if eos_id is not None and ids[-1] == eos_id:
            truncated[-1] = eos_id
        return truncated

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        
        prompt_ids_raw = self.tokenizer.encode_instruction(row['instruction'])
        code_ids_raw = self.tokenizer.encode_code(row['code'])
        
        prompt_ids = self._pad_or_truncate(prompt_ids_raw, self.max_prompt_len)
        code_ids = self._pad_or_truncate_code(code_ids_raw, self.max_code_len)
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


def log_generated_samples(
    model,
    tokenizer,
    samples,
    device,
    epoch,
    steps=50,
    experiment=None,
    checkpoint_dir=None,
    total_epochs=None,
    mask_bounds=None,
    max_code_len=None,
):
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
            if mask_bounds is not None:
                lower_bound, upper_bound = mask_bounds
            elif total_epochs is None:
                lower_bound, upper_bound = 0.30, 1.0
            else:
                lower_bound, upper_bound = get_epoch_mask_bounds(epoch, total_epochs)
            mask_prob = sample_epoch_mask_prob(1, device, lower_bound, upper_bound)
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
                    max_code_len=max_code_len,
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
        experiment.log_table(f"generated_samples_epoch_{epoch}.csv", table_rows, step=epoch)

    model.train()


def cleanup_checkpoint_dir(checkpoint_dir, keep_path=None):
    """Keep only the selected checkpoint file in checkpoints/.

    Removes all diffcoder_best*.pt files except keep_path.
    """
    if keep_path is not None and not keep_path.name.startswith("diffcoder_best"):
        return

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
    resume_fixed_mask_epochs=0,
    use_dtw_loss=False,
    dtw_loss_weight=0.0,
    monitor_mask_bounds=(0.30, 0.50),
    generation_mask_bounds=(0.90, 1.00),
    generation_monitor_weight=0.70,
    high_mask_batch_prob=0.10,
    high_mask_train_bounds=(0.90, 1.00),
    generation_eval_samples=None,
    generation_eval_interval=5,
    generation_eval_steps=50,
    generation_eval_max_code_len=256,
    max_prompt_len=96,
):
    use_amp = device == "cuda"
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp)
    if best_val_loss is None:
        best_val_loss = float("inf")
    # total epochs used to compute epoch-dependent masking schedule
    effective_total_epochs = total_epochs or epochs
    latest_checkpoint_path = checkpoint_dir / "diffcoder_latest.pt"

    # training bookkeeping
    epochs_without_improvement = max(0, int(epochs_without_improvement))
    if not (0.0 <= generation_monitor_weight <= 1.0):
        raise ValueError("generation_monitor_weight must be in [0, 1].")
    if not (0.0 <= high_mask_batch_prob <= 1.0):
        raise ValueError("high_mask_batch_prob must be in [0, 1].")
    for name, bounds in {
        "monitor_mask_bounds": monitor_mask_bounds,
        "generation_mask_bounds": generation_mask_bounds,
        "high_mask_train_bounds": high_mask_train_bounds,
    }.items():
        if not (0.0 <= bounds[0] <= bounds[1] <= 1.0):
            raise ValueError(f"{name} must satisfy 0 <= lower <= upper <= 1.")

    loss_embedding_matrix = resolve_loss_embedding_matrix(model) if use_dtw_loss else None
    if use_dtw_loss and loss_embedding_matrix is None:
        print("Ostrzezenie: USE_DTW_LOSS jest wlaczone, ale model nie ma macierzy embeddingow. Uzywam samego CE.")
        dtw_loss_weight = 0.0

    # CE is the default objective. The DTW term is opt-in because it changes the
    # scale of the loss and should be monitored separately.
    loss_fn = CalculateLoss(
        gamma=1.0,
        ce_weight=1.0,
        dtw_weight=dtw_loss_weight if use_dtw_loss else 0.0,
        embedding_matrix=loss_embedding_matrix,
    ).to(device)
    
    for epoch in range(start_epoch, epochs):
        model.train()
        total_loss = 0
        total_ce_loss = 0.0
        total_dtw_loss = 0.0
        total_masked_tokens = 0
        total_candidate_tokens = 0
        total_high_mask_samples = 0
        total_train_samples = 0
        epoch_number = epoch + 1
        current_mask_lower_bound, current_mask_upper_bound = get_resume_mask_bounds(
            epoch_number,
            effective_total_epochs,
            start_epoch,
            resume_fixed_mask_epochs,
        )
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

            mask_prob = sample_epoch_mask_prob(batch_size, device, current_mask_lower_bound, current_mask_upper_bound)
            if high_mask_batch_prob > 0.0:
                use_high_mask = torch.rand(batch_size, device=device) < high_mask_batch_prob
                high_mask_prob = sample_epoch_mask_prob(
                    batch_size,
                    device,
                    high_mask_train_bounds[0],
                    high_mask_train_bounds[1],
                )
                mask_prob = torch.where(use_high_mask, high_mask_prob, mask_prob)
                total_high_mask_samples += int(use_high_mask.sum().item())
            total_train_samples += batch_size
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
                ast_embeddings = build_ast_embeddings(batch, device, loss_fn)

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
            total_ce_loss += ce_loss.item()
            total_dtw_loss += dtw_loss.item()
            total_masked_tokens += int(is_masked.sum().item())
            total_candidate_tokens += int((x_0 != model.pad_token_id).sum().item())
            progress_bar.set_postfix({'loss': f"{current_loss:.4f}"})
            if experiment is not None:
                step = epoch * len(train_dataloader) + batch_idx
                experiment.log_metric("train_loss", current_loss, step=step)
                
        avg_loss = total_loss / len(train_dataloader)
        avg_ce_loss = total_ce_loss / len(train_dataloader)
        avg_dtw_loss = total_dtw_loss / len(train_dataloader)
        train_masked_ratio = total_masked_tokens / max(1, total_candidate_tokens)
        train_high_mask_sample_ratio = total_high_mask_samples / max(1, total_train_samples)

        current_val_metrics = evaluate_diffcoder_loss(
            model,
            val_dataloader,
            loss_fn,
            device,
            (current_mask_lower_bound, current_mask_upper_bound),
            use_amp,
        )
        monitor_val_metrics = evaluate_diffcoder_loss(
            model,
            val_dataloader,
            loss_fn,
            device,
            monitor_mask_bounds,
            use_amp,
        )
        generation_val_metrics = evaluate_diffcoder_loss(
            model,
            val_dataloader,
            loss_fn,
            device,
            generation_mask_bounds,
            use_amp,
        )
        val_loss = current_val_metrics["loss"]
        denoise_monitor_val_loss = monitor_val_metrics["loss"]
        generation_val_loss = generation_val_metrics["loss"]
        monitor_val_loss = (
            (1.0 - generation_monitor_weight) * denoise_monitor_val_loss
            + generation_monitor_weight * generation_val_loss
        )
        generation_quality_metrics = None
        if (
            generation_eval_samples
            and generation_eval_interval > 0
            and (epoch_number == 1 or epoch_number % generation_eval_interval == 0)
        ):
            generation_quality_metrics = evaluate_generation_quality(
                model=model,
                tokenizer=tokenizer,
                samples=generation_eval_samples,
                device=device,
                steps=generation_eval_steps,
                max_code_len=generation_eval_max_code_len,
                max_prompt_len=max_prompt_len,
            )

        print(f"\n--- Zakończono Epokę {epoch+1} | Średni błąd: {avg_loss:.4f} ---")
        print(f"Średni loss w epoce {epoch+1}: {avg_loss:.6f}")
        print(
            f"Train CE: {avg_ce_loss:.6f} | Train DTW: {avg_dtw_loss:.6f} | "
            f"masked tokens: {train_masked_ratio * 100:.2f}% | "
            f"high-mask samples: {train_high_mask_sample_ratio * 100:.2f}%"
        )
        print(f"Walidacyjny loss przy aktualnym maskowaniu w epoce {epoch+1}: {val_loss:.6f}")
        print(
            f"Denoise monitor val loss ({monitor_mask_bounds[0] * 100:.1f}% - "
            f"{monitor_mask_bounds[1] * 100:.1f}% maskowania): {denoise_monitor_val_loss:.6f}"
        )
        print(
            f"Generation val loss ({generation_mask_bounds[0] * 100:.1f}% - "
            f"{generation_mask_bounds[1] * 100:.1f}% maskowania): {generation_val_loss:.6f}"
        )
        print(
            f"Combined monitor val loss "
            f"(generation weight {generation_monitor_weight:.2f}): {monitor_val_loss:.6f}"
        )
        if generation_quality_metrics is not None:
            print(
                "Generation compile monitor "
                f"({generation_quality_metrics['sample_count']} samples, "
                f"steps={generation_eval_steps}, max_len={generation_eval_max_code_len}): "
                f"compile={generation_quality_metrics['compile_pass_rate']:.2%} | "
                f"parse={generation_quality_metrics['parse_pass_rate']:.2%} | "
                f"EOS={generation_quality_metrics['eos_rate']:.2%} | "
                f"avg tokens={generation_quality_metrics['avg_generated_tokens']:.1f}"
            )

        previous_lr = optimizer.param_groups[0]["lr"]
        if scheduler is not None:
            scheduler.step(monitor_val_loss)
        current_lr = optimizer.param_groups[0]["lr"]

        if experiment is not None:
            experiment.log_metric("epoch_loss", avg_loss, step=epoch + 1)
            experiment.log_metric("epoch_avg_loss", avg_loss, step=epoch + 1)
            experiment.log_metric("epoch_ce_loss", avg_ce_loss, step=epoch + 1)
            experiment.log_metric("epoch_dtw_loss", avg_dtw_loss, step=epoch + 1)
            experiment.log_metric("epoch_mask_lower", current_mask_lower_bound, step=epoch + 1)
            experiment.log_metric("epoch_mask_upper", current_mask_upper_bound, step=epoch + 1)
            experiment.log_metric(
                "epoch_mask_mean",
                (current_mask_lower_bound + current_mask_upper_bound) / 2,
                step=epoch + 1,
            )
            experiment.log_metric("epoch_masked_token_ratio", train_masked_ratio, step=epoch + 1)
            experiment.log_metric("epoch_high_mask_sample_ratio", train_high_mask_sample_ratio, step=epoch + 1)
            experiment.log_metric("val_loss", val_loss, step=epoch + 1)
            experiment.log_metric("val_ce_loss", current_val_metrics["ce_loss"], step=epoch + 1)
            experiment.log_metric("val_dtw_loss", current_val_metrics["dtw_loss"], step=epoch + 1)
            experiment.log_metric(
                "val_masked_token_ratio",
                current_val_metrics["masked_token_ratio"],
                step=epoch + 1,
            )
            experiment.log_metric("monitor_val_loss", monitor_val_loss, step=epoch + 1)
            experiment.log_metric("denoise_monitor_val_loss", denoise_monitor_val_loss, step=epoch + 1)
            experiment.log_metric("denoise_monitor_val_ce_loss", monitor_val_metrics["ce_loss"], step=epoch + 1)
            experiment.log_metric("denoise_monitor_val_dtw_loss", monitor_val_metrics["dtw_loss"], step=epoch + 1)
            experiment.log_metric(
                "denoise_monitor_val_masked_token_ratio",
                monitor_val_metrics["masked_token_ratio"],
                step=epoch + 1,
            )
            experiment.log_metric("monitor_mask_lower", monitor_mask_bounds[0], step=epoch + 1)
            experiment.log_metric("monitor_mask_upper", monitor_mask_bounds[1], step=epoch + 1)
            experiment.log_metric("generation_val_loss", generation_val_loss, step=epoch + 1)
            experiment.log_metric("generation_val_ce_loss", generation_val_metrics["ce_loss"], step=epoch + 1)
            experiment.log_metric("generation_val_dtw_loss", generation_val_metrics["dtw_loss"], step=epoch + 1)
            experiment.log_metric(
                "generation_val_masked_token_ratio",
                generation_val_metrics["masked_token_ratio"],
                step=epoch + 1,
            )
            experiment.log_metric("generation_mask_lower", generation_mask_bounds[0], step=epoch + 1)
            experiment.log_metric("generation_mask_upper", generation_mask_bounds[1], step=epoch + 1)
            experiment.log_metric("generation_monitor_weight", generation_monitor_weight, step=epoch + 1)
            experiment.log_metric("high_mask_batch_prob", high_mask_batch_prob, step=epoch + 1)
            experiment.log_metric("high_mask_train_lower", high_mask_train_bounds[0], step=epoch + 1)
            experiment.log_metric("high_mask_train_upper", high_mask_train_bounds[1], step=epoch + 1)
            if generation_quality_metrics is not None:
                experiment.log_metric(
                    "generation_compile_pass_rate",
                    generation_quality_metrics["compile_pass_rate"],
                    step=epoch + 1,
                )
                experiment.log_metric(
                    "generation_parse_pass_rate",
                    generation_quality_metrics["parse_pass_rate"],
                    step=epoch + 1,
                )
                experiment.log_metric(
                    "generation_eos_rate",
                    generation_quality_metrics["eos_rate"],
                    step=epoch + 1,
                )
                experiment.log_metric(
                    "generation_avg_tokens",
                    generation_quality_metrics["avg_generated_tokens"],
                    step=epoch + 1,
                )
                experiment.log_metric(
                    "generation_avg_chars",
                    generation_quality_metrics["avg_generated_chars"],
                    step=epoch + 1,
                )
            experiment.log_metric("lr", current_lr, step=epoch + 1)

        if current_lr < previous_lr:
            print(f"ReduceLROnPlateau obniżył lr: {previous_lr:.8f} -> {current_lr:.8f}")

        improved = monitor_val_loss < best_val_loss
        if improved:
            best_val_loss = monitor_val_loss
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1

        checkpoint = {
            "epoch": epoch + 1,
            "total_epochs": effective_total_epochs,
            "monitor_objective_version": MONITOR_OBJECTIVE_VERSION,
            "mask_lower_bound": current_mask_lower_bound,
            "mask_upper_bound": current_mask_upper_bound,
            "val_loss": val_loss,
            "monitor_val_loss": monitor_val_loss,
            "denoise_monitor_val_loss": denoise_monitor_val_loss,
            "generation_val_loss": generation_val_loss,
            "monitor_mask_lower_bound": monitor_mask_bounds[0],
            "monitor_mask_upper_bound": monitor_mask_bounds[1],
            "generation_mask_lower_bound": generation_mask_bounds[0],
            "generation_mask_upper_bound": generation_mask_bounds[1],
            "generation_monitor_weight": generation_monitor_weight,
            "high_mask_batch_prob": high_mask_batch_prob,
            "high_mask_train_lower_bound": high_mask_train_bounds[0],
            "high_mask_train_upper_bound": high_mask_train_bounds[1],
            "generation_eval_interval": generation_eval_interval,
            "generation_eval_steps": generation_eval_steps,
            "generation_eval_max_code_len": generation_eval_max_code_len,
            "generation_eval_samples": 0 if generation_eval_samples is None else len(generation_eval_samples),
            "tokenizer_vocab_size": model.vocab_size,
            "tokenizer_pad_token_id": model.pad_token_id,
            "tokenizer_eos_token_id": tokenizer.eos_token_id,
            "tokenizer_mask_token_id": model.mask_token_id,
            "tokenizer_pad_equals_eos": model.pad_token_id == tokenizer.eos_token_id,
            "best_val_loss": best_val_loss,
            "best_monitor_loss": best_val_loss,
            "epochs_without_improvement": epochs_without_improvement,
            "use_dtw_loss": use_dtw_loss,
            "dtw_loss_weight": loss_fn.dtw_weight,
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
                experiment.log_other("best_model_monitor_val_loss", monitor_val_loss)
                experiment.log_other("best_model_generation_val_loss", generation_val_loss)
                experiment.log_model(
                    name="diffcoder_best",
                    file_or_folder=str(checkpoint_path),
                    overwrite=True,
                )

            best_checkpoint_path = checkpoint_path
        else:
            print(
                f"Brak poprawy monitor val loss przez {epochs_without_improvement} epok(e). "
                f"Najlepszy monitor val loss: {best_val_loss:.6f}"
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
                mask_bounds=(current_mask_lower_bound, current_mask_upper_bound),
                max_code_len=generation_eval_max_code_len,
            )

        if epochs_without_improvement >= early_stopping_patience:
            print(
                f"Early stopping: brak poprawy monitor val loss przez {early_stopping_patience} epok. "
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
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", "4"))
    ACCUMULATION_STEPS = int(os.getenv("ACCUMULATION_STEPS", "8"))
    NUM_WORKERS = int(os.getenv("NUM_WORKERS", "3"))
    EPOCHS = int(os.getenv("EPOCHS", "500"))
    VAL_SPLIT = 0.05
    EARLY_STOPPING_PATIENCE = int(os.getenv("EARLY_STOPPING_PATIENCE", "100"))
    HIDDEN_DIM = 512
    NUM_BLOCKS = 6
    DILATION_FACTOR = int(os.getenv("DILATION_FACTOR", "2"))
    DATASET_FRACTION = float(os.getenv("DATASET_FRACTION", "1.0")) # size of dataset
    BASE_LR = float(os.getenv("BASE_LR", "5e-6"))
    LR_SCHEDULER_FACTOR = 0.5
    LR_SCHEDULER_PATIENCE = 8
    LR_SCHEDULER_MIN_LR = 1e-6
    LR_SCHEDULER_THRESHOLD = 1e-4
    LR_SCHEDULER_COOLDOWN = 2
    RESUME_FROM_CHECKPOINT = parse_bool_env("RESUME_FROM_CHECKPOINT", default=True)
    WARM_START_MODEL_ONLY = parse_bool_env("WARM_START_MODEL_ONLY", default=True)
    RESUME_CHECKPOINT_NAME = os.getenv("RESUME_CHECKPOINT_NAME", "")
    RESUME_CHECKPOINT_PATH = os.getenv("RESUME_CHECKPOINT_PATH", "")
    RESUME_FIXED_MASK_EPOCHS = int(os.getenv("RESUME_FIXED_MASK_EPOCHS", "15"))
    USE_DTW_LOSS = parse_bool_env("USE_DTW_LOSS", default=False)
    DTW_LOSS_WEIGHT = float(os.getenv("DTW_LOSS_WEIGHT", "0.1" if USE_DTW_LOSS else "0.0"))
    MONITOR_MASK_LOWER = float(os.getenv("MONITOR_MASK_LOWER", "0.30"))
    MONITOR_MASK_UPPER = float(os.getenv("MONITOR_MASK_UPPER", "0.50"))
    if not (0.0 <= MONITOR_MASK_LOWER <= MONITOR_MASK_UPPER <= 1.0):
        raise ValueError("MONITOR_MASK_LOWER and MONITOR_MASK_UPPER must satisfy 0 <= lower <= upper <= 1.")
    GENERATION_MASK_LOWER = float(os.getenv("GENERATION_MASK_LOWER", "0.90"))
    GENERATION_MASK_UPPER = float(os.getenv("GENERATION_MASK_UPPER", "1.00"))
    if not (0.0 <= GENERATION_MASK_LOWER <= GENERATION_MASK_UPPER <= 1.0):
        raise ValueError(
            "GENERATION_MASK_LOWER and GENERATION_MASK_UPPER must satisfy 0 <= lower <= upper <= 1."
        )
    GENERATION_MONITOR_WEIGHT = float(os.getenv("GENERATION_MONITOR_WEIGHT", "0.85"))
    if not (0.0 <= GENERATION_MONITOR_WEIGHT <= 1.0):
        raise ValueError("GENERATION_MONITOR_WEIGHT must be in [0, 1].")
    HIGH_MASK_BATCH_PROB = float(os.getenv("HIGH_MASK_BATCH_PROB", "0.50"))
    if not (0.0 <= HIGH_MASK_BATCH_PROB <= 1.0):
        raise ValueError("HIGH_MASK_BATCH_PROB must be in [0, 1].")
    HIGH_MASK_TRAIN_LOWER = float(os.getenv("HIGH_MASK_TRAIN_LOWER", str(GENERATION_MASK_LOWER)))
    HIGH_MASK_TRAIN_UPPER = float(os.getenv("HIGH_MASK_TRAIN_UPPER", str(GENERATION_MASK_UPPER)))
    if not (0.0 <= HIGH_MASK_TRAIN_LOWER <= HIGH_MASK_TRAIN_UPPER <= 1.0):
        raise ValueError(
            "HIGH_MASK_TRAIN_LOWER and HIGH_MASK_TRAIN_UPPER must satisfy 0 <= lower <= upper <= 1."
        )
    GENERATION_EVAL_SAMPLES = int(os.getenv("GENERATION_EVAL_SAMPLES", "5"))
    GENERATION_EVAL_INTERVAL = int(os.getenv("GENERATION_EVAL_INTERVAL", "5"))
    GENERATION_EVAL_STEPS = int(os.getenv("GENERATION_EVAL_STEPS", "50"))
    GENERATION_EVAL_MAX_CODE_LEN = int(os.getenv("GENERATION_EVAL_MAX_CODE_LEN", "256"))

    tokenizer = CodeTokenizer()

    comet_api_key = os.getenv("COMET_API_KEY")
    comet_project_name = os.getenv("COMET_PROJECT_NAME")
    comet_workspace = os.getenv("COMET_WORKSPACE")
    comet_disabled = parse_bool_env("COMET_DISABLED", default=False)

    experiment = None
    if not comet_disabled and Experiment is not None and comet_api_key and comet_project_name:
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
            "warm_start_model_only": WARM_START_MODEL_ONLY,
            "lr_scheduler_factor": LR_SCHEDULER_FACTOR,
            "lr_scheduler_patience": LR_SCHEDULER_PATIENCE,
            "lr_scheduler_min_lr": LR_SCHEDULER_MIN_LR,
            "lr_scheduler_threshold": LR_SCHEDULER_THRESHOLD,
            "lr_scheduler_cooldown": LR_SCHEDULER_COOLDOWN,
            "use_dtw_loss": USE_DTW_LOSS,
            "dtw_loss_weight": DTW_LOSS_WEIGHT,
            "monitor_mask_lower": MONITOR_MASK_LOWER,
            "monitor_mask_upper": MONITOR_MASK_UPPER,
            "generation_mask_lower": GENERATION_MASK_LOWER,
            "generation_mask_upper": GENERATION_MASK_UPPER,
            "generation_monitor_weight": GENERATION_MONITOR_WEIGHT,
            "high_mask_batch_prob": HIGH_MASK_BATCH_PROB,
            "high_mask_train_lower": HIGH_MASK_TRAIN_LOWER,
            "high_mask_train_upper": HIGH_MASK_TRAIN_UPPER,
            "generation_eval_samples": GENERATION_EVAL_SAMPLES,
            "generation_eval_interval": GENERATION_EVAL_INTERVAL,
            "generation_eval_steps": GENERATION_EVAL_STEPS,
            "generation_eval_max_code_len": GENERATION_EVAL_MAX_CODE_LEN,
            "tokenizer_vocab_size": tokenizer.vocab_size,
            "tokenizer_pad_token_id": tokenizer.pad_token_id,
            "tokenizer_eos_token_id": tokenizer.eos_token_id,
            "tokenizer_mask_token_id": tokenizer.mask_token_id,
            "tokenizer_pad_equals_eos": tokenizer.pad_token_id == tokenizer.eos_token_id,
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
    checkpoint_dir_env = os.getenv("CHECKPOINT_DIR", "checkpoints_generation")
    checkpoint_dir = Path(checkpoint_dir_env)
    if not checkpoint_dir.is_absolute():
        checkpoint_dir = repo_root / checkpoint_dir
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
        if RESUME_CHECKPOINT_PATH:
            resume_path = Path(RESUME_CHECKPOINT_PATH)
            if not resume_path.is_absolute():
                resume_path = repo_root / resume_path
        elif RESUME_CHECKPOINT_NAME:
            resume_path = checkpoint_dir / RESUME_CHECKPOINT_NAME
        else:
            resume_path = resolve_resume_checkpoint(checkpoint_dir)
            legacy_best_checkpoint = repo_root / "checkpoints" / "diffcoder_best.pt"
            if resume_path is None and legacy_best_checkpoint.exists():
                resume_path = legacy_best_checkpoint
        if resume_path is not None and resume_path.exists():
            checkpoint = torch.load(resume_path, map_location=DEVICE)
            vocab_adaptation = adapt_state_dict_to_tokenizer(
                checkpoint["model_state_dict"],
                target_vocab_size=tokenizer.vocab_size,
                pad_token_id=tokenizer.pad_token_id,
                mask_token_id=tokenizer.mask_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )
            model.load_state_dict(vocab_adaptation.state_dict)
            if vocab_adaptation.changed or WARM_START_MODEL_ONLY:
                print(
                    "Warm start z wag modelu checkpointu. "
                    f"vocab: {vocab_adaptation.source_vocab_size} -> {vocab_adaptation.target_vocab_size}. "
                    "Resetuje optimizer, scheduler i liczniki treningu. "
                    "Ustaw WARM_START_MODEL_ONLY=0, aby wznowic pelny stan treningu."
                )
                start_epoch = 0
                training_total_epochs = EPOCHS
                best_val_loss = None
                epochs_without_improvement = 0
            else:
                optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
                monitor_config_matches = checkpoint_monitor_config_matches(
                    checkpoint,
                    (MONITOR_MASK_LOWER, MONITOR_MASK_UPPER),
                    (GENERATION_MASK_LOWER, GENERATION_MASK_UPPER),
                    GENERATION_MONITOR_WEIGHT,
                )
                scheduler_state_dict = checkpoint.get("scheduler_state_dict")
                if scheduler_state_dict is not None and monitor_config_matches:
                    scheduler.load_state_dict(scheduler_state_dict)
                elif scheduler_state_dict is not None:
                    print(
                        "Resetuje stan scheduler'a, bo zapisany checkpoint uzywal innego monitor objective."
                    )
                start_epoch = int(checkpoint.get("epoch", 0))
                training_total_epochs = int(checkpoint.get("total_epochs", EPOCHS))
                if monitor_config_matches and "best_monitor_loss" in checkpoint:
                    best_val_loss = float(checkpoint["best_monitor_loss"])
                    epochs_without_improvement = int(checkpoint.get("epochs_without_improvement", 0))
                else:
                    best_val_loss = None
                    epochs_without_improvement = 0
                    print(
                        "Resetuje licznik monitor val loss, bo checkpoint nie ma zgodnego "
                        "generation-blended monitor objective."
                    )
            best_checkpoint_path = resume_path if not (vocab_adaptation.changed or WARM_START_MODEL_ONLY) else None
            cleanup_checkpoint_dir(checkpoint_dir, keep_path=resume_path)
            best_loss_text = "nowy baseline" if best_val_loss is None else f"{best_val_loss:.6f}"
            print(
                f"Wznawiam trening z checkpointu: {resume_path} | "
                f"epoch={start_epoch} | total_epochs={training_total_epochs} | "
                f"best_monitor_loss={best_loss_text} | lr={optimizer.param_groups[0]['lr']:.8f}"
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

    generation_eval_samples = []
    if GENERATION_EVAL_SAMPLES > 0 and len(val_dataset) > 0:
        rng = random.Random(123)
        val_source_indices = list(getattr(val_dataset, "indices", range(len(val_dataset))))
        chosen_indices = rng.sample(
            val_source_indices,
            min(GENERATION_EVAL_SAMPLES, len(val_source_indices)),
        )
        for idx in chosen_indices:
            row = dataset.df.iloc[idx]
            generation_eval_samples.append(
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
        resume_fixed_mask_epochs=RESUME_FIXED_MASK_EPOCHS if RESUME_FROM_CHECKPOINT else 0,
        use_dtw_loss=USE_DTW_LOSS,
        dtw_loss_weight=DTW_LOSS_WEIGHT,
        monitor_mask_bounds=(MONITOR_MASK_LOWER, MONITOR_MASK_UPPER),
        generation_mask_bounds=(GENERATION_MASK_LOWER, GENERATION_MASK_UPPER),
        generation_monitor_weight=GENERATION_MONITOR_WEIGHT,
        high_mask_batch_prob=HIGH_MASK_BATCH_PROB,
        high_mask_train_bounds=(HIGH_MASK_TRAIN_LOWER, HIGH_MASK_TRAIN_UPPER),
        generation_eval_samples=generation_eval_samples,
        generation_eval_interval=GENERATION_EVAL_INTERVAL,
        generation_eval_steps=GENERATION_EVAL_STEPS,
        generation_eval_max_code_len=GENERATION_EVAL_MAX_CODE_LEN,
        max_prompt_len=MAX_PROMPT_LEN,
    )

    if experiment is not None:
        experiment.end()
