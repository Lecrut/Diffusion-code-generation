from datetime import datetime
import json
import math
from pathlib import Path
import os
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import gc 
import numpy as np
import random
from torch.utils.data import DataLoader
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor, EarlyStopping, Callback
from pytorch_lightning.loggers import CometLogger
from dotenv import load_dotenv

from diffusion.model import LocalConvDiffCoder
from tokenizer import CodeTokenizer 
from diffusion.loss import CalculateLoss, aligned_multi_reference_cross_entropy
from diffusion.masking import (
    CodeCorruptor,
    MixtureMaskSampler,
    MixtureMaskSamplerConfig,
    NoiseRegimeConfig,
    TopologyConfig,
    ratio_from_counts,
)
from diffusion.metrics import (
    ast_validity_rate,
    compile_validity_rate,
    levenshtein_distance,
    normalized_levenshtein_distance,
)
from tokenized_dataset import (
    TokenizedMemmapDataset,
    collate_tokenized_batch,
    ensure_tokenized_cache,
    load_cached_samples,
    make_train_val_indices,
    tokenized_cache_dir,
)

import sys
env_test_path = Path(__file__).resolve().parent.parent / ".env.test"
# is_testing = (
#     os.getenv("USE_TEST_ENV") == "1"
#     or os.getenv("DIFFCODER_TEST") == "1"
#     or os.getenv("PYTEST_CURRENT_TEST") is not None
#     or "pytest" in sys.modules
#     or "unittest" in sys.modules
# )
is_testing = False
if is_testing and env_test_path.exists():
    load_dotenv(dotenv_path=env_test_path, override=True)
else:
    load_dotenv()



def sample_epoch_mask_prob(batch_size, device, lower_bound, upper_bound):
    return lower_bound + torch.rand(batch_size, device=device) * (upper_bound - lower_bound)


def mask_bin_metric_name(mask_prob: float) -> str:
    return f"val_loss_mask_{int(round(mask_prob * 100)):02d}"


def pad_or_truncate_ids(token_ids, max_length, pad_token_id):
    token_ids = list(token_ids)[:max_length]
    if len(token_ids) < max_length:
        token_ids.extend([pad_token_id] * (max_length - len(token_ids)))
    return token_ids


def adjacent_repeat_fraction(token_ids):
    if len(token_ids) <= 1:
        return 0.0
    repeats = sum(1 for left, right in zip(token_ids, token_ids[1:]) if left == right)
    return repeats / (len(token_ids) - 1)



# --- LEGACY MODULE & CALLBACKS REMOVED ---


class ThroughputLoggerCallback(Callback):
    def __init__(self, every_n_batches=50):
        super().__init__()
        self.every_n_batches = every_n_batches
        self._last_time = None
        self._examples_since_log = 0

    def on_train_start(self, trainer, pl_module):
        self._last_time = time.perf_counter()
        self._examples_since_log = 0
        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()

    def on_train_batch_end(self, trainer, pl_module, outputs, batch, batch_idx):
        if not trainer.is_global_zero or self.every_n_batches <= 0:
            return

        batch_size = int(batch["code_ids"].size(0)) if isinstance(batch, dict) else 0
        self._examples_since_log += batch_size

        current_batch = batch_idx + 1
        if current_batch % self.every_n_batches != 0:
            return

        now = time.perf_counter()
        elapsed = max(now - (self._last_time or now), 1e-6)
        examples_per_sec = self._examples_since_log / elapsed
        self._last_time = now
        self._examples_since_log = 0

        loss_value = None
        if isinstance(outputs, dict):
            loss_value = outputs.get("loss")
        elif torch.is_tensor(outputs):
            loss_value = outputs
        if torch.is_tensor(loss_value):
            loss_value = float(loss_value.detach().cpu())

        memory_msg = ""
        if torch.cuda.is_available():
            allocated_gb = torch.cuda.memory_allocated() / (1024 ** 3)
            peak_gb = torch.cuda.max_memory_allocated() / (1024 ** 3)
            memory_msg = f" | vram={allocated_gb:.2f}GB peak={peak_gb:.2f}GB"

        loss_msg = "" if loss_value is None else f" | loss={loss_value:.4f}"
        print(
            f"[TRAIN] global_step={trainer.global_step} batch={current_batch} "
            f"| {examples_per_sec:.1f} examples/s{loss_msg}{memory_msg}"
        )

    def on_validation_end(self, trainer, pl_module):
        self._last_time = time.perf_counter()
        self._examples_since_log = 0


class ResetEarlyStoppingOnResumeCallback(Callback):
    def __init__(self, enabled=False):
        super().__init__()
        self.enabled = bool(enabled)
        self._done = False

    def on_fit_start(self, trainer, pl_module):
        if not self.enabled or self._done:
            return

        for callback in trainer.callbacks:
            if isinstance(callback, EarlyStopping):
                callback.wait_count = 0
                callback.stopped_epoch = 0
                initial_best = (
                    float("inf")
                    if callback.mode == "min"
                    else -float("inf")
                )
                callback.best_score = torch.tensor(
                    initial_best,
                    device=pl_module.device,
                )
                print(f"[RESUME] Reset EarlyStopping state for this resumed run. Mode: {callback.mode}, Best Score: {initial_best}")
        self._done = True


# --- CUSTOM CALLBACK DO LOGOWANIA GENERACJI ---

class LogGeneratedSamplesCallback(Callback):
    def __init__(
        self,
        sample_pairs,
        tokenizer,
        every_n_steps=5000,
        console_chars=1200,
        generation_steps=50,
        max_prompt_len=None,
        max_code_len=None,
    ):
        super().__init__()
        self.samples = sample_pairs
        self.tokenizer = tokenizer
        self.every_n_steps = every_n_steps
        self.console_chars = console_chars
        self.generation_steps = int(generation_steps)
        self.max_prompt_len = None if max_prompt_len is None else int(max_prompt_len)
        self.max_code_len = None if max_code_len is None else int(max_code_len)
        self._last_logged_step = None
        self._last_logged_bucket = None

    def _should_log(self, trainer):
        if not self.samples:
            return False
        if self.every_n_steps <= 0:
            return True
        step = int(getattr(trainer, "global_step", 0))
        if step < self.every_n_steps:
            return False
        bucket = step // self.every_n_steps
        return bucket != self._last_logged_bucket

    def _clip_for_console(self, text):
        if self.console_chars <= 0 or len(text) <= self.console_chars:
            return text
        return text[: self.console_chars] + "\n... <truncated>"

    def _prompt_tensor(self, prompt, device):
        prompt_ids = self.tokenizer.encode_instruction(prompt)
        if self.max_prompt_len is not None:
            prompt_ids = pad_or_truncate_ids(prompt_ids, self.max_prompt_len, self.tokenizer.pad_token_id)
        return torch.tensor(prompt_ids, dtype=torch.long, device=device).unsqueeze(0)

    def _code_tensor(self, code, device, model):
        max_code_len = self.max_code_len
        if max_code_len is None:
            max_code_len = max(model.max_seq_len - (self.max_prompt_len or 0), 1)
        code_ids = self.tokenizer.encode_code(code)[:max_code_len]
        padded_ids = pad_or_truncate_ids(code_ids, max_code_len, self.tokenizer.pad_token_id)
        return torch.tensor([padded_ids], dtype=torch.long, device=device), len(code_ids), max_code_len

    def on_validation_epoch_end(self, trainer, pl_module):
        if trainer.sanity_checking:
            return
        if not self._should_log(trainer):
            return
        self._last_logged_step = int(trainer.global_step)
        if self.every_n_steps > 0:
            self._last_logged_bucket = self._last_logged_step // self.every_n_steps

        pl_module.eval()
        epoch = pl_module.current_epoch + 1
        device = pl_module.device
        table_rows = []
        
        comet_logger = None
        for logger in trainer.loggers:
            if isinstance(logger, CometLogger):
                comet_logger = logger.experiment
                break

        for idx, sample in enumerate(self.samples):
            prompt = sample["instruction"]
            target_code = sample["code"]
            prompt_ids = self._prompt_tensor(prompt, device)

            try:
                x_0, code_len, max_code_len = self._code_tensor(target_code, device, pl_module.model)

                # Temporarily save and seed for deterministic masking (Cause 19)
                orig_rng_state = torch.get_rng_state()
                orig_cuda_rng_state = torch.cuda.get_rng_state() if torch.cuda.is_available() else None
                
                seed_val = pl_module.validation_seed + idx
                torch.manual_seed(seed_val)
                if torch.cuda.is_available():
                    torch.cuda.manual_seed_all(seed_val)

                sampler_output = pl_module.mask_sampler.sample(1, device)
                corruption = pl_module.corruptor.corrupt(x_0, sampler_output.mask_prob)

                # Restore random state
                torch.set_rng_state(orig_rng_state)
                if orig_cuda_rng_state is not None:
                    torch.cuda.set_rng_state(orig_cuda_rng_state)

                x_masked = corruption.input_ids
                is_masked = corruption.target_mask
                display_len = max(code_len, 1)
                masked_text = self.tokenizer.decode(
                    x_masked[0, :display_len].tolist(),
                    skip_special_tokens=False,
                )

                with torch.no_grad():
                    logits = pl_module.model(x_masked, prompt_ids, sampler_output.mask_prob.view(-1))
                    logits = pl_module.model._prepare_generation_logits(
                        logits,
                        eos_token_id=self.tokenizer.code_eos_token_id,
                        forbidden_token_ids=self.tokenizer.special_token_ids,
                    )
                    pred_ids = logits.argmax(dim=-1)
                    
                    mask_id = self.tokenizer.mask_token_id
                    x_masked_cpu = x_masked[0].cpu().tolist()
                    pred_cpu = pred_ids[0].cpu().tolist()
                    mask_cpu = is_masked[0].cpu().tolist()
                    merged = []
                    for pos, tok in enumerate(x_masked_cpu):
                        if tok == mask_id and mask_cpu[pos]:
                            merged.append(pred_cpu[pos])
                        else:
                            merged.append(tok)
                    predicted_text = self.tokenizer.decode(
                        merged[:display_len],
                        skip_special_tokens=False,
                    )
            except Exception as e:
                masked_text = f"<ERROR: {type(e).__name__}: {e}>"
                predicted_text = masked_text

            try:
                with torch.no_grad():
                    gen_ids = pl_module.model.generate(
                        prompt_ids,
                        steps=self.generation_steps,
                        device=device,
                        eos_token_id=self.tokenizer.code_eos_token_id,
                        # Use the target length for this diagnostic sample; otherwise
                        # a missed CODE_EOS turns the 512-token pad window into noise.
                        code_len=code_len,
                        forbidden_token_ids=self.tokenizer.special_token_ids,
                        **pl_module.generation_config,
                    )
                gen_text = self.tokenizer.decode(gen_ids[0].tolist())
            except Exception as e:
                gen_text = f"<ERROR: {type(e).__name__}: {e}>"

            print("-" * 80)
            print(
                f"[SAMPLE] global_step={trainer.global_step} epoch={epoch} sample={idx}\n"
                f"PROMPT:\n{self._clip_for_console(prompt)}\n\n"
                f"GROUND_TRUTH:\n{self._clip_for_console(target_code)}\n\n"
                f"MASKED_GROUND_TRUTH:\n{self._clip_for_console(masked_text)}\n\n"
                f"PREDICTED_THIS_ITERATION:\n{self._clip_for_console(predicted_text)}\n\n"
                f"GENERATED:\n{self._clip_for_console(gen_text)}"
            )

            if comet_logger is not None:
                comet_logger.log_text(
                    f"Global step {trainer.global_step} | epoch {epoch} | sample {idx}"
                    f"\nPROMPT:\n{prompt}\n\nGROUND_TRUTH:\n{target_code}"
                    f"\n\nMASKED_GROUND_TRUTH:\n{masked_text}\n\nPREDICTED_THIS_ITERATION:\n{predicted_text}"
                    f"\n\nGENERATED:\n{gen_text}",
                    step=trainer.global_step,
                )
                table_rows.append({
                    "global_step": trainer.global_step, "epoch": epoch, "sample": idx, "prompt": prompt, "ground_truth": target_code,
                    "masked_ground_truth": masked_text, "predicted_this_iteration": predicted_text, "generated": gen_text
                })

        if comet_logger is not None and table_rows:
            comet_logger.log_table("generated_samples.csv", table_rows, step=trainer.global_step)
            
        pl_module.train()


class CometCheckpointUploadCallback(Callback):
    def __init__(self, best_checkpoint_callback, last_checkpoint_callback, mode="min"):
        super().__init__()
        self.best_checkpoint_callback = best_checkpoint_callback
        self.last_checkpoint_callback = last_checkpoint_callback
        self.mode = mode
        self._uploaded_best_score = None
        self._uploaded_best_path = ""

    def _get_comet_experiment(self, trainer):
        for logger in trainer.loggers:
            if isinstance(logger, CometLogger):
                return logger.experiment
        return None

    def _upload_model(self, experiment, model_name, model_path):
        if not model_path or not os.path.isfile(model_path):
            return False
        experiment.log_model(model_name, model_path, overwrite=True)
        return True

    def on_validation_epoch_end(self, trainer, pl_module):
        if trainer.sanity_checking:
            return

        experiment = self._get_comet_experiment(trainer)
        if experiment is None:
            return

        best_path = self.best_checkpoint_callback.best_model_path
        best_score = self.best_checkpoint_callback.best_model_score
        if not best_path or best_score is None:
            return

        best_score_value = float(best_score.item() if hasattr(best_score, "item") else best_score)
        if self._uploaded_best_score is None:
            is_improved = True
        elif self.mode == "max":
            is_improved = best_score_value > self._uploaded_best_score
        else:
            is_improved = best_score_value < self._uploaded_best_score
        is_new_path = best_path != self._uploaded_best_path

        if is_improved or is_new_path:
            if self._upload_model(experiment, "LocalConvDiffCoder-best", best_path):
                self._uploaded_best_score = best_score_value
                self._uploaded_best_path = best_path
                print(f">>> [COMET] Zapisano BEST model ({self.best_checkpoint_callback.monitor}={best_score_value:.6f}) z nadpisaniem. <<<")

    def on_train_epoch_end(self, trainer, pl_module):
        if trainer.sanity_checking:
            return

        experiment = self._get_comet_experiment(trainer)
        if experiment is None:
            return

        last_path = getattr(self.last_checkpoint_callback, "last_model_path", "") or self.last_checkpoint_callback.best_model_path
        if self._upload_model(experiment, "LocalConvDiffCoder-last", last_path):
            print(
                f">>> [COMET] Zapisano LAST model z epoki {trainer.current_epoch + 1} z nadpisaniem. <<<"
            )


# --- GŁÓWNY PROCES TRENINGOWY ---

class MixedDiffCoderLightning(pl.LightningModule):
    def __init__(
        self,
        model,
        tokenizer,
        mask_sampler,
        corruptor,
        *,
        validation_mask_bins,
        validation_seed=42,
        validation_samples=None,
        fixed_prompt_eval_samples=5,
        fixed_prompt_eval_every_n_epochs=1,
        fixed_generation_code_len=None,
        ast_eval_samples=100,
        ast_generation_steps=50,
        ast_every_n_steps=1000,
        ast_log_failures=3,
        generation_config=None,
        validation_logit_chunk_size=1024,
        mask_telemetry_every_n_steps=50,
        max_prompt_len=None,
        max_code_len=None,
        prompt_shuffle_diagnostic=False,
        prompt_shuffle_mask_prob=1.0,
        reference_cache_dir=None,
        multi_reference_loss=False,
        multi_reference_max_refs=32,
        train_logit_chunk_size=1024,
        lr_warmup_steps=1000,
        min_lr=1e-6,
        base_lr=5e-5,
        weight_decay=0.01,
        rollback_stage=None,
        use_ast_loss=True,
        ast_loss_base_weight=0.1,
        ast_loss_scale=0.4,
        max_ast_len=256,
        ast_dtw_max_code_len=64,
        ast_dtw_max_ast_len=64,
        ast_loss_every_n_steps=8,
        ast_loss_probability=1.0,
        prompt_contrastive_loss=True,
        prompt_contrastive_weight=0.25,
        prompt_contrastive_margin=0.25,
        prompt_contrastive_mask_prob=1.0,
        focal_loss_gamma=1.5,
        batch_token_weighting=True,
        batch_token_weight_min=0.25,
        batch_token_weight_max=4.0,
    ):
        super().__init__()
        self.model = model
        self.tokenizer = tokenizer
        self.mask_sampler = mask_sampler
        self.corruptor = corruptor
        self.validation_mask_bins = tuple(float(value) for value in validation_mask_bins)
        self.validation_seed = int(validation_seed)
        self.validation_samples = list(validation_samples or [])
        self.fixed_prompt_eval_samples = int(fixed_prompt_eval_samples)
        self.fixed_prompt_eval_every_n_epochs = int(fixed_prompt_eval_every_n_epochs)
        fixed_generation_code_len = 0 if fixed_generation_code_len is None else int(fixed_generation_code_len)
        self.fixed_generation_code_len = None if fixed_generation_code_len <= 0 else fixed_generation_code_len
        self.ast_eval_samples = int(ast_eval_samples)
        self.ast_generation_steps = int(ast_generation_steps)
        self.ast_every_n_steps = int(ast_every_n_steps)
        self.ast_log_failures = int(ast_log_failures)
        self.generation_config = generation_config or {}
        self.validation_logit_chunk_size = int(validation_logit_chunk_size)
        self.mask_telemetry_every_n_steps = int(mask_telemetry_every_n_steps)
        self.max_prompt_len = None if max_prompt_len is None else int(max_prompt_len)
        self.max_code_len = None if max_code_len is None else int(max_code_len)
        self.prompt_shuffle_diagnostic = bool(prompt_shuffle_diagnostic)
        self.prompt_shuffle_mask_prob = float(prompt_shuffle_mask_prob)
        self.reference_cache_dir = None if reference_cache_dir is None else str(reference_cache_dir)
        self.multi_reference_loss = bool(multi_reference_loss)
        self.multi_reference_max_refs = int(multi_reference_max_refs)
        self.train_logit_chunk_size = int(train_logit_chunk_size)
        self._reference_code_ids = None
        self._reference_code_lens = None
        self._group_ref_offsets = None
        self.lr_warmup_steps = int(lr_warmup_steps)
        self.min_lr = float(min_lr)
        self.base_lr = base_lr
        self.weight_decay = weight_decay
        self.rollback_stage = rollback_stage
        self.use_ast_loss = use_ast_loss
        self.ast_loss_base_weight = float(ast_loss_base_weight)
        self.ast_loss_scale = float(ast_loss_scale)
        self.max_ast_len = int(max_ast_len)
        self.ast_dtw_max_code_len = int(ast_dtw_max_code_len)
        self.ast_dtw_max_ast_len = int(ast_dtw_max_ast_len)
        self.ast_loss_every_n_steps = int(ast_loss_every_n_steps)
        self.ast_loss_probability = float(ast_loss_probability)
        self.prompt_contrastive_loss = bool(prompt_contrastive_loss)
        self.prompt_contrastive_weight = float(prompt_contrastive_weight)
        self.prompt_contrastive_margin = float(prompt_contrastive_margin)
        self.prompt_contrastive_mask_prob = float(prompt_contrastive_mask_prob)
        self.focal_loss_gamma = float(focal_loss_gamma)
        self.batch_token_weighting = bool(batch_token_weighting)
        self.batch_token_weight_min = float(batch_token_weight_min)
        self.batch_token_weight_max = float(batch_token_weight_max)
        self._val_loss_sums = None
        self._val_token_counts = None
        self._prompt_shuffle_loss_sum = None
        self._prompt_shuffle_token_count = None
        self._last_ast_eval_step = None
        self._last_fixed_prompt_eval_epoch = None
        self._last_ast_eval_metrics = None

        # Load AST Vocabulary and initialize AST node embedding layer
        self.ast_vocab = None
        self.ast_vocab_size = None
        if self.use_ast_loss:
            if self.reference_cache_dir is None:
                raise RuntimeError("AST loss is enabled, but reference_cache_dir is None.")
            vocab_path = Path(self.reference_cache_dir) / "ast_vocab.json"
            if not vocab_path.is_file():
                raise RuntimeError(f"AST loss is enabled, but vocabulary path {vocab_path} does not exist.")
            try:
                with open(vocab_path, "r", encoding="utf-8") as f:
                    self.ast_vocab = json.load(f)
            except Exception as e:
                raise RuntimeError(f"AST loss is enabled, but failed to load {vocab_path}: {e}")

            if not self.ast_vocab:
                raise RuntimeError(f"AST loss is enabled, but AST vocabulary loaded from {vocab_path} is empty.")

            # Calculate vocab size based on max value to support non-contiguous IDs correctly
            self.ast_vocab_size = max(self.ast_vocab.values()) + 1

            # Validate IDs and padding index
            min_id = min(self.ast_vocab.values())
            if min_id < 0:
                raise RuntimeError(f"AST vocabulary contains invalid negative index: {min_id}")

            pad_id = self.ast_vocab.get("PAD", 0)
            if pad_id >= self.ast_vocab_size:
                raise RuntimeError(
                    f"AST vocabulary padding ID ({pad_id}) is out of bounds for vocab size {self.ast_vocab_size}"
                )

            print(f"[AST] Loaded AST vocabulary with size {self.ast_vocab_size}")

        embedding_layer = getattr(model, "token_embedding", getattr(model, "embedding", None)) if use_ast_loss else None
        
        if self.use_ast_loss:
            embedding_dim = embedding_layer.weight.shape[1] if embedding_layer is not None else self.model.hidden_dim
            pad_id = self.ast_vocab.get("PAD", 0) if self.ast_vocab else 0
            self.ast_embedding = nn.Embedding(
                self.ast_vocab_size,
                embedding_dim,
                padding_idx=pad_id,
            )

        self.loss_fn = CalculateLoss(
            gamma=1.0,
            ce_weight=1.0,
            dtw_weight=1.0 if use_ast_loss else 0.0,
            embedding_matrix=embedding_layer.weight if embedding_layer is not None else None,
            max_dtw_code_len=self.ast_dtw_max_code_len,
            max_dtw_ast_len=self.ast_dtw_max_ast_len,
        )

    def _token_ce_loss(self, logits, targets, *, reduction="mean"):
        if targets.numel() == 0:
            return logits.new_zeros(())
        token_loss = F.cross_entropy(logits, targets, reduction="none")

        if self.focal_loss_gamma > 0.0:
            pt = torch.exp(-token_loss).clamp(1e-6, 1.0)
            token_loss = ((1.0 - pt) ** self.focal_loss_gamma) * token_loss

        if self.batch_token_weighting:
            counts = torch.bincount(targets.detach(), minlength=self.tokenizer.vocab_size).float()
            target_counts = counts[targets].clamp_min(1.0)
            weights = target_counts.rsqrt()
            weights = weights / weights.mean().clamp_min(1e-6)
            weights = weights.clamp(self.batch_token_weight_min, self.batch_token_weight_max)
            token_loss = token_loss * weights

        if reduction == "sum":
            return token_loss.sum()
        if reduction == "mean":
            return token_loss.mean()
        if reduction == "none":
            return token_loss
        raise ValueError(f"Unsupported reduction: {reduction}")

    def _get_ast_embeddings(self, batch):
        if self.use_ast_loss:
            required = {"ast_node_ids", "ast_length", "code_len"}
            missing = {k for k in required if k not in batch or batch[k] is None}
            if missing:
                raise RuntimeError(
                    f"AST loss enabled, but batch is missing: {sorted(missing)}"
                )
        if "ast_node_ids" not in batch or batch.get("ast_node_ids") is None:
            print("[AST] Warning: 'ast_node_ids' not found in batch. Returning None for AST embeddings.")
            return None
        ast_node_ids = batch.get("ast_node_ids").to(self.device)
        return self.ast_embedding(ast_node_ids)

    def _load_reference_cache(self):
        if not self.multi_reference_loss or self.reference_cache_dir is None:
            return False
        if self._reference_code_ids is not None:
            return True

        cache_dir = Path(self.reference_cache_dir)
        required = [
            cache_dir / "reference_code_ids.npy",
            cache_dir / "reference_code_lens.npy",
            cache_dir / "group_ref_offsets.npy",
        ]
        if not all(path.is_file() for path in required):
            try:
                trainer = self.trainer
            except RuntimeError:
                trainer = None
            if trainer is None or getattr(trainer, "is_global_zero", True):
                print(f"[MULTI-REF WARNING] Reference cache files missing in {cache_dir}; using exact CE.")
            return False

        self._reference_code_ids = np.load(required[0], mmap_mode="r")
        self._reference_code_lens = np.load(required[1], mmap_mode="r")
        self._group_ref_offsets = np.load(required[2], mmap_mode="r")
        return True



    def _can_use_multi_reference_loss(self, batch):
        return (
            self.multi_reference_loss
            and "group_id" in batch
            and "code_len" in batch
            and self._load_reference_cache()
        )

    def _ce_from_masked_features(self, masked_features, masked_targets, *, chunk_size, reduction="mean"):
        if masked_targets.numel() == 0:
            return masked_features.new_zeros(())
        if chunk_size is None or chunk_size <= 0 or masked_features.size(0) <= chunk_size:
            logits = self.model.lm_head(masked_features)
            return self._token_ce_loss(logits, masked_targets, reduction=reduction)

        loss_sum = masked_features.new_zeros((), dtype=torch.float32)
        token_count = 0
        for start in range(0, masked_features.size(0), int(chunk_size)):
            end = min(start + int(chunk_size), masked_features.size(0))
            logits = self.model.lm_head(masked_features[start:end])
            loss_sum = loss_sum + self._token_ce_loss(logits, masked_targets[start:end], reduction="sum")
            token_count += end - start

        if reduction == "sum":
            return loss_sum
        if reduction == "mean":
            return loss_sum / max(token_count, 1)
        raise ValueError(f"Unsupported reduction: {reduction}")

    def _multi_reference_loss_from_corruption(self, batch, x_t, target_mask, t, *, reduction="mean", code_features=None):
        x_0 = batch["code_ids"]
        prompt_ids = batch["prompt_ids"]
        if code_features is None:
            code_features = self.model.forward_features(x_t, prompt_ids, t)
        total_loss = code_features.new_zeros(())
        total_tokens = 0

        # GPU-to-CPU optimization to prevent repeated GPU-CPU synchronization stalls (Cause 13)
        token_counts = target_mask.sum(dim=1).detach().cpu().tolist()

        for row, token_count in enumerate(token_counts):
            if token_count == 0:
                continue
            row_mask = target_mask[row]

            row_features = self.model.ln_final(code_features[row, row_mask])
            row_logits = self.model.lm_head(row_features)
            row_loss = aligned_multi_reference_cross_entropy(
                masked_logits=row_logits,
                x_0=x_0[row : row + 1],
                x_t=x_t[row : row + 1],
                target_mask=row_mask.unsqueeze(0),
                code_lens=batch["code_len"][row : row + 1],
                group_ids=batch["group_id"][row : row + 1],
                reference_code_ids=self._reference_code_ids,
                reference_code_lens=self._reference_code_lens,
                group_ref_offsets=self._group_ref_offsets,
                max_refs_per_group=self.multi_reference_max_refs,
                reduction="sum",
            )
            total_loss = total_loss + row_loss
            total_tokens += token_count

        if reduction == "sum":
            return total_loss
        if reduction == "mean":
            return total_loss / max(total_tokens, 1)
        raise ValueError(f"Unsupported reduction: {reduction}")

    def _exact_ce_from_corruption(
        self,
        batch,
        x_t,
        target_mask,
        t,
        *,
        prompt_ids=None,
        reduction="mean",
        chunk_size=None,
    ):
        x_0 = batch["code_ids"]
        prompt_ids = batch["prompt_ids"] if prompt_ids is None else prompt_ids
        masked_targets = x_0[target_mask]
        if masked_targets.numel() == 0:
            return x_t.new_zeros(())
        code_features = self.model.forward_features(x_t, prompt_ids, t)
        masked_features = self.model.ln_final(code_features[target_mask])
        return self._ce_from_masked_features(
            masked_features,
            masked_targets,
            chunk_size=self.train_logit_chunk_size if chunk_size is None else chunk_size,
            reduction=reduction,
        )

    def _loss_from_corruption(self, batch, x_t, target_mask, t):
        x_0 = batch["code_ids"]
        prompt_ids = batch["prompt_ids"]
        masked_targets = x_0[target_mask]

        if masked_targets.numel() == 0:
            return torch.tensor(0.0, device=self.device, requires_grad=True)

        if not self.use_ast_loss:
            if self._can_use_multi_reference_loss(batch):
                return self._multi_reference_loss_from_corruption(batch, x_t, target_mask, t)
            return self._exact_ce_from_corruption(batch, x_t, target_mask, t)

        code_features = self.model.forward_features(x_t, prompt_ids, t)
        expected_repr = self.model.ln_final(code_features)
        masked_features = expected_repr[target_mask]

        # 1. Compute selected CE loss (Cause 6)
        if self._can_use_multi_reference_loss(batch):
            ce_loss = self._multi_reference_loss_from_corruption(
                batch, x_t, target_mask, t, reduction="mean", code_features=code_features
            )
        else:
            ce_loss = self._ce_from_masked_features(
                masked_features,
                masked_targets,
                chunk_size=self.train_logit_chunk_size,
                reduction="mean",
            )

        # Determine whether AST should run on this batch.
        calculate_ast = True
        if self.training:
            step_ok = (
                    self.ast_loss_every_n_steps <= 1
                    or self.global_step % self.ast_loss_every_n_steps == 0
            )
            prob_ok = (
                    self.ast_loss_probability >= 1.0
                    or random.random() < self.ast_loss_probability
            )
            calculate_ast = step_ok and prob_ok

        # Completely skip all AST-related work.
        if not calculate_ast:
            return ce_loss

        ast_embeddings = self._get_ast_embeddings(batch)

        mean_mask_ratio = t.detach().mean()
        dynamic_dtw_weight = (
                self.ast_loss_base_weight
                + self.ast_loss_scale * mean_mask_ratio
        )

        code_lengths = batch["code_len"].to(self.device)
        ast_lengths = batch["ast_length"].to(self.device)

        total_loss, _, dtw_loss = self.loss_fn(
            expected_repr=expected_repr,
            masked_logits=None,
            masked_targets=masked_targets,
            ast_embeddings=ast_embeddings,
            code_lengths=code_lengths,
            ast_lengths=ast_lengths,
            dtw_weight=dynamic_dtw_weight,
            ce_loss=ce_loss,
        )

        # Shape assertions for diagnostics validation (Task 9 & 10)
        if self.use_ast_loss and ast_embeddings is not None and calculate_ast:
            assert expected_repr.ndim == 3, f"expected_repr must be 3D [B, N, E], got {expected_repr.shape}"
            assert ast_embeddings.ndim == 3, f"ast_embeddings must be 3D [B, M, E], got {ast_embeddings.shape}"
            assert expected_repr.size(-1) == ast_embeddings.size(-1), f"Embedding dim mismatch: expected_repr={expected_repr.shape}, ast_embeddings={ast_embeddings.shape}"
            assert ast_embeddings.size(1) > 1 or (ast_lengths == 1).all(), f"AST is single-node or unexpectedly pooled: ast_embeddings={ast_embeddings.shape}"

        # Diagnostics Logging (Task 10)
        # Log once near the start of training
        if self.global_step == 0 and self.use_ast_loss and ast_embeddings is not None:
            trainer = getattr(self, "trainer", None)
            if trainer is None or getattr(trainer, "is_global_zero", True):
                print("\n" + "="*80)
                print("[AST LOSS DIAGNOSTICS] Shapes at training start:")
                print(f" - expected_repr shape:    {expected_repr.shape}")
                print(f" - ast_embeddings shape:   {ast_embeddings.shape}")
                if code_lengths is not None:
                    print(f" - code_lengths range:     {code_lengths.min().item()} to {code_lengths.max().item()}")
                if ast_lengths is not None:
                    print(f" - ast_lengths range:      {ast_lengths.min().item()} to {ast_lengths.max().item()}")
                print("="*80 + "\n")

        # Periodically log loss contributions and sequence length distributions
        if (
                self.use_ast_loss
                and self.mask_telemetry_every_n_steps > 0
                and self.global_step % self.mask_telemetry_every_n_steps == 0
        ):
            self.log("train_ast_loss_ce", ce_loss, on_step=True, on_epoch=False)
            self.log("train_ast_loss_dtw_raw", dtw_loss, on_step=True, on_epoch=False)
            self.log("train_ast_loss_dtw_weight", dynamic_dtw_weight, on_step=True, on_epoch=False)
            self.log("train_ast_loss_dtw_weighted_contrib", dynamic_dtw_weight * dtw_loss, on_step=True, on_epoch=False)
            if code_lengths is not None:
                self.log("train_ast_loss_mean_code_len", code_lengths.float().mean(), on_step=True, on_epoch=False)
            if ast_lengths is not None:
                self.log("train_ast_loss_mean_ast_len", ast_lengths.float().mean(), on_step=True, on_epoch=False)
                self.log("train_ast_loss_max_ast_len", ast_lengths.float().max(), on_step=True, on_epoch=False)

        return total_loss

    def _log_training_mask_metrics(self, sampler_output, corruption):
        if self.mask_telemetry_every_n_steps <= 0:
            return
        trainer = getattr(self, "trainer", None)
        if trainer is not None and int(trainer.global_step) % self.mask_telemetry_every_n_steps != 0:
            return

        batch_size = corruption.input_ids.size(0)
        self.log("train_mask_prob_mean", sampler_output.mask_prob.mean(), on_step=True, on_epoch=False, batch_size=batch_size)
        self.log("train_realized_mask_ratio", corruption.realized_mask_ratio.mean(), on_step=True, on_epoch=False, batch_size=batch_size)
        actual_ratio = ratio_from_counts(corruption.masked_counts.sum(), corruption.eligible_counts.sum())
        self.log("train_actual_eligible_mask_fraction", actual_ratio, on_step=True, on_epoch=False, batch_size=batch_size)

        for idx, name in enumerate(sampler_output.regime_names):
            value = (sampler_output.regime_ids == idx).float().mean()
            self.log(f"train_mask_regime_{name}", value, on_step=True, on_epoch=False, batch_size=batch_size)

        bucket_edges = [(0.0, 0.35), (0.35, 0.65), (0.65, 0.85), (0.85, 1.01)]
        for low, high in bucket_edges:
            value = ((sampler_output.mask_prob >= low) & (sampler_output.mask_prob < high)).float().mean()
            self.log(f"train_mask_bucket_{int(low * 100):02d}_{int(min(high, 1.0) * 100):02d}", value, on_step=True, on_epoch=False, batch_size=batch_size)

        for idx, name in enumerate(corruption.topology_names):
            value = (corruption.topology_ids == idx).float().mean()
            self.log(f"train_topology_{name}", value, on_step=True, on_epoch=False, batch_size=batch_size)

        prefix_selected = (corruption.topology_ids == 2).float()
        prefix_mean = (corruption.visible_prefix_fraction * prefix_selected).sum() / prefix_selected.sum().clamp_min(1.0)
        suffix_selected = (corruption.topology_ids == 3).float()
        suffix_mean = (corruption.truncated_suffix_fraction * suffix_selected).sum() / suffix_selected.sum().clamp_min(1.0)
        self.log("train_visible_prefix_fraction", prefix_mean, on_step=True, on_epoch=False, batch_size=batch_size)
        self.log("train_truncated_suffix_fraction", suffix_mean, on_step=True, on_epoch=False, batch_size=batch_size)

        valid_block = (corruption.block_length_ids >= 0).float()
        for idx, length in enumerate(corruption.block_lengths):
            value = (corruption.block_length_ids == idx).float().sum() / valid_block.sum().clamp_min(1.0)
            self.log(f"train_block_length_{length}", value, on_step=True, on_epoch=False, batch_size=batch_size)

    def training_step(self, batch, batch_idx):
        x_0 = batch["code_ids"]
        sampler_output = self.mask_sampler.sample(x_0.size(0), self.device)
        corruption = self.corruptor.corrupt(x_0, sampler_output.mask_prob)
        loss = self._loss_from_corruption(
            batch,
            corruption.input_ids,
            corruption.target_mask,
            sampler_output.mask_prob.view(-1),
        )
        contrastive_penalty = None
        if (
                self.prompt_contrastive_loss
                and self.prompt_contrastive_weight > 0.0
                and x_0.size(0) > 1
        ):
            contrastive_t = torch.full(
                (x_0.size(0),),
                self.prompt_contrastive_mask_prob,
                device=self.device,
            )
            contrastive_corruption = self.corruptor.corrupt(x_0, contrastive_t)
            shuffled_prompt_ids = batch["prompt_ids"].roll(shifts=1, dims=0)
            correct_ce = self._exact_ce_from_corruption(
                batch,
                contrastive_corruption.input_ids,
                contrastive_corruption.target_mask,
                contrastive_t,
                reduction="mean",
            )
            shuffled_ce = self._exact_ce_from_corruption(
                batch,
                contrastive_corruption.input_ids,
                contrastive_corruption.target_mask,
                contrastive_t,
                prompt_ids=shuffled_prompt_ids,
                reduction="mean",
            )
            contrastive_penalty = torch.relu(
                self.prompt_contrastive_margin + correct_ce - shuffled_ce
            )
            loss = loss + (self.prompt_contrastive_weight * contrastive_penalty)
            self.log("train_prompt_contrastive_correct_ce", correct_ce, on_step=True, on_epoch=False, batch_size=x_0.size(0))
            self.log("train_prompt_contrastive_shuffled_ce", shuffled_ce, on_step=True, on_epoch=False, batch_size=x_0.size(0))
            self.log("train_prompt_contrastive_delta", shuffled_ce - correct_ce, on_step=True, on_epoch=False, batch_size=x_0.size(0))
            self.log("train_prompt_contrastive_penalty", contrastive_penalty, on_step=True, on_epoch=False, batch_size=x_0.size(0))
        self.log("train_loss", loss, on_step=True, on_epoch=True, prog_bar=False, batch_size=x_0.size(0))
        self._log_training_mask_metrics(sampler_output, corruption)
        return loss

    def on_train_epoch_start(self):
        if self.trainer.is_global_zero:
            regimes = ", ".join(
                f"{regime.name}:{regime.low:.2f}-{regime.high:.2f}@{regime.weight:.2f}"
                for regime in self.mask_sampler.config.regimes
            )
            print(f"\n[Mixed Masking] Epoch {self.current_epoch + 1} | {regimes}")

    def on_validation_epoch_start(self):
        n_bins = len(self.validation_mask_bins)
        self._val_loss_sums = torch.zeros(n_bins, device=self.device, dtype=torch.float32)
        self._val_token_counts = torch.zeros(n_bins, device=self.device, dtype=torch.long)
        
        self._prompt_shuffle_loss_sum = torch.zeros((), device=self.device, dtype=torch.float32)
        self._prompt_non_shuffle_loss_sum = torch.zeros((), device=self.device, dtype=torch.float32)
        self._prompt_shuffle_token_count = torch.zeros((), device=self.device, dtype=torch.long)

        # Training-distribution validation loss metrics (Cause 5 & 17)
        self._val_dist_ce_loss_sum = 0.0
        self._val_dist_masked_token_count = 0
        self._val_dist_dtw_loss_sum = 0.0
        self._val_dist_sample_count = 0
        self._val_dist_dtw_weight_sum = 0.0

    def validation_step(self, batch, batch_idx):
        x_0 = batch["code_ids"]
        prompt_ids = batch["prompt_ids"]
        sample_ids = batch["sample_id"]

        # A. Training-distribution validation loss (Cause 5 & 17)
        # Seed PyTorch for determinism based on validation_seed and batch_idx
        orig_rng_state = torch.get_rng_state()
        orig_cuda_rng_state = torch.cuda.get_rng_state() if torch.cuda.is_available() else None
        
        seed_val = self.validation_seed + batch_idx
        torch.manual_seed(seed_val)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed_val)

        # Sample and corrupt exactly as in training
        sampler_output = self.mask_sampler.sample(x_0.size(0), self.device)
        corruption = self.corruptor.corrupt(x_0, sampler_output.mask_prob)

        # Restore random state immediately
        torch.set_rng_state(orig_rng_state)
        if orig_cuda_rng_state is not None:
            torch.cuda.set_rng_state(orig_cuda_rng_state)

        # Calculate loss on training-distribution corruption
        dist_x_t = corruption.input_ids
        dist_mask = corruption.target_mask
        dist_t = sampler_output.mask_prob.view(-1)
        dist_masked_targets = x_0[dist_mask]

        if dist_masked_targets.numel() > 0:
            if not self.use_ast_loss:
                # Use standard or multi-ref CE
                if self._can_use_multi_reference_loss(batch):
                    dist_ce_loss = self._multi_reference_loss_from_corruption(batch, dist_x_t, dist_mask, dist_t, reduction="mean")
                else:
                    dist_ce_loss = self._exact_ce_from_corruption(
                        batch,
                        dist_x_t,
                        dist_mask,
                        dist_t,
                        reduction="mean",
                        chunk_size=self.validation_logit_chunk_size,
                    )
                dist_dtw_loss = torch.tensor(0.0, device=self.device)
                dist_dynamic_dtw_weight = 0.0
            else:
                dist_features = self.model.forward_features(dist_x_t, prompt_ids, dist_t)
                expected_repr_v = self.model.ln_final(dist_features)
                dist_masked_features = expected_repr_v[dist_mask]
                
                if self._can_use_multi_reference_loss(batch):
                    dist_ce_loss = self._multi_reference_loss_from_corruption(
                        batch, dist_x_t, dist_mask, dist_t, reduction="mean", code_features=dist_features
                    )
                else:
                    dist_ce_loss = self._ce_from_masked_features(
                        dist_masked_features,
                        dist_masked_targets,
                        chunk_size=self.validation_logit_chunk_size,
                        reduction="mean",
                    )
                
                dist_ast_embeddings = self._get_ast_embeddings(batch)
                dist_mean_mask_ratio = dist_t.detach().mean()
                dist_dynamic_dtw_weight = self.ast_loss_base_weight + self.ast_loss_scale * dist_mean_mask_ratio
                
                dist_code_lens = batch.get("code_len").to(self.device) if "code_len" in batch else None
                dist_ast_lens = batch.get("ast_length").to(self.device) if "ast_length" in batch else None
                
                _, _, dist_dtw_loss = self.loss_fn(
                    expected_repr=expected_repr_v,
                    masked_logits=None,
                    masked_targets=dist_masked_targets,
                    ast_embeddings=dist_ast_embeddings,
                    code_lengths=dist_code_lens,
                    ast_lengths=dist_ast_lens,
                    dtw_weight=dist_dynamic_dtw_weight,
                    ce_loss=dist_ce_loss,
                )
                
            # Accumulate CE loss at token level
            num_masked_tokens = int(dist_masked_targets.numel())
            self._val_dist_ce_loss_sum += dist_ce_loss.detach().item() * num_masked_tokens
            self._val_dist_masked_token_count += num_masked_tokens
            
            # Accumulate DTW loss and weight at sample level
            num_samples = int(x_0.size(0))
            self._val_dist_dtw_loss_sum += dist_dtw_loss.detach().item() * num_samples
            self._val_dist_sample_count += num_samples
            
            dtw_w = dist_dynamic_dtw_weight.item() if isinstance(dist_dynamic_dtw_weight, torch.Tensor) else float(dist_dynamic_dtw_weight)
            self._val_dist_dtw_weight_sum += dtw_w * num_samples

        # B. Fixed bins validation (macro CE)
        for bin_idx, mask_prob in enumerate(self.validation_mask_bins):
            target_mask = self.corruptor.deterministic_independent_mask(
                x_0,
                mask_prob,
                sample_ids,
                bin_index=bin_idx,
                seed=self.validation_seed,
            )
            masked_targets = x_0[target_mask]
            if masked_targets.numel() == 0:
                continue

            x_t = x_0.clone()
            x_t[target_mask] = self.model.mask_token_id
            t = torch.full((x_0.size(0),), float(mask_prob), device=self.device)
            if self._can_use_multi_reference_loss(batch):
                loss_sum = self._multi_reference_loss_from_corruption(batch, x_t, target_mask, t, reduction="sum")
            else:
                loss_sum = self._exact_ce_from_corruption(
                    batch,
                    x_t,
                    target_mask,
                    t,
                    reduction="sum",
                    chunk_size=self.validation_logit_chunk_size,
                )
            self._val_loss_sums[bin_idx] += loss_sum.detach().float()
            self._val_token_counts[bin_idx] += int(masked_targets.numel())

        # C. Shuffled prompt diagnostic (Apples-to-apples) (Cause 9)
        if self.prompt_shuffle_diagnostic and x_0.size(0) > 1:
            mask_prob = float(self.prompt_shuffle_mask_prob)
            target_mask = self.corruptor.deterministic_independent_mask(
                x_0,
                mask_prob,
                sample_ids,
                bin_index=len(self.validation_mask_bins) + 17,
                seed=self.validation_seed,
            )
            masked_targets = x_0[target_mask]
            if masked_targets.numel() > 0:
                x_t = x_0.clone()
                x_t[target_mask] = self.model.mask_token_id
                shuffled_prompt_ids = prompt_ids.roll(shifts=1, dims=0)
                t = torch.full((x_0.size(0),), mask_prob, device=self.device)
                
                # Non-shuffle standard CE pass
                non_shuffle_sum = self._exact_ce_from_corruption(
                    batch,
                    x_t,
                    target_mask,
                    t,
                    prompt_ids=prompt_ids,
                    reduction="sum",
                    chunk_size=self.validation_logit_chunk_size,
                )
                # Shuffle standard CE pass
                shuffle_sum = self._exact_ce_from_corruption(
                    batch,
                    x_t,
                    target_mask,
                    t,
                    prompt_ids=shuffled_prompt_ids,
                    reduction="sum",
                    chunk_size=self.validation_logit_chunk_size,
                )
                
                self._prompt_shuffle_loss_sum += shuffle_sum.detach().float()
                self._prompt_non_shuffle_loss_sum += non_shuffle_sum.detach().float()
                self._prompt_shuffle_token_count += int(masked_targets.numel())

    def on_validation_epoch_end(self):
        if self._val_loss_sums is None or self._val_token_counts is None:
            return

        loss_sums = self._val_loss_sums
        token_counts = self._val_token_counts
        if self.trainer.world_size > 1:
            loss_sums = self.all_gather(loss_sums).sum(dim=0)
            token_counts = self.all_gather(token_counts).sum(dim=0)

        losses = loss_sums / token_counts.clamp_min(1).float()
        valid_bins = token_counts > 0
        aggregate = losses[valid_bins].mean() if valid_bins.any() else torch.tensor(0.0, device=self.device)

        for bin_idx, mask_prob in enumerate(self.validation_mask_bins):
            metric_name = mask_bin_metric_name(mask_prob)
            self.log(metric_name, losses[bin_idx], prog_bar=bin_idx == 0, sync_dist=True)
            self.log(f"val_tokens_mask_{int(round(mask_prob * 100)):02d}", token_counts[bin_idx].float(), sync_dist=True)

        # Log training-distribution losses (Cause 5 & 17)
        if self._val_dist_sample_count > 0:
            if self.trainer.world_size > 1:
                val_ce_sum = self.all_gather(torch.tensor(self._val_dist_ce_loss_sum, device=self.device)).sum().item()
                val_masked_tokens = self.all_gather(torch.tensor(self._val_dist_masked_token_count, device=self.device)).sum().item()
                val_dtw_sum = self.all_gather(torch.tensor(self._val_dist_dtw_loss_sum, device=self.device)).sum().item()
                val_sample_count = self.all_gather(torch.tensor(self._val_dist_sample_count, device=self.device)).sum().item()
                val_dtw_weight_sum = self.all_gather(torch.tensor(self._val_dist_dtw_weight_sum, device=self.device)).sum().item()
            else:
                val_ce_sum = self._val_dist_ce_loss_sum
                val_masked_tokens = float(self._val_dist_masked_token_count)
                val_dtw_sum = self._val_dist_dtw_loss_sum
                val_sample_count = float(self._val_dist_sample_count)
                val_dtw_weight_sum = self._val_dist_dtw_weight_sum
                
            val_ce_loss = val_ce_sum / max(val_masked_tokens, 1.0)
            self.log("val_ce_loss", val_ce_loss, prog_bar=True, sync_dist=True)

            if self.use_ast_loss:
                val_dtw_loss = val_dtw_sum / max(val_sample_count, 1.0)
                val_mean_dtw_weight = val_dtw_weight_sum / max(val_sample_count, 1.0)
                # Explicitly aggregate total loss aligned with the dataset objective.
                val_total_loss = val_ce_loss + val_mean_dtw_weight * val_dtw_loss
                self.log("val_dtw_loss", val_dtw_loss, sync_dist=True)
                self.log("val_total_loss", val_total_loss, sync_dist=True)
                val_loss = val_total_loss
            else:
                val_loss = val_ce_loss

            # val_loss is training-distribution validation loss (Cause 17)
            self.log("val_loss", val_loss, prog_bar=True, sync_dist=True)

        self.log("val_fixed_bin_macro_ce", aggregate, prog_bar=True, sync_dist=True)
        self._log_prompt_shuffle_diagnostic()
        self._evaluate_ast_validation_samples()

    def _log_prompt_shuffle_diagnostic(self):
        if not self.prompt_shuffle_diagnostic:
            return
        loss_sum = self._prompt_shuffle_loss_sum
        non_shuffle_loss_sum = self._prompt_non_shuffle_loss_sum
        token_count = self._prompt_shuffle_token_count
        if loss_sum is None or non_shuffle_loss_sum is None or token_count is None:
            return
        if self.trainer.world_size > 1:
            loss_sum = self.all_gather(loss_sum).sum()
            non_shuffle_loss_sum = self.all_gather(non_shuffle_loss_sum).sum()
            token_count = self.all_gather(token_count).sum()
        if int(token_count.item()) <= 0:
            return

        shuffle_loss = loss_sum / token_count.clamp_min(1).float()
        non_shuffle_loss = non_shuffle_loss_sum / token_count.clamp_min(1).float()
        suffix = int(round(self.prompt_shuffle_mask_prob * 100))
        self.log(f"val_prompt_shuffle_loss_mask_{suffix:02d}", shuffle_loss, sync_dist=True)
        self.log(
            f"val_prompt_shuffle_loss_delta_mask_{suffix:02d}",
            shuffle_loss - non_shuffle_loss,
            sync_dist=True,
        )

    def _fixed_generation_length(self, prompt_len: int, target_code_len: int | None = None) -> int:
        max_available = max(int(self.model.max_seq_len) - int(prompt_len), 1)
        if self.fixed_generation_code_len is not None:
            return min(int(self.fixed_generation_code_len), max_available)
        if target_code_len is not None and int(target_code_len) > 0:
            return min(int(target_code_len), max_available)
        if self.max_code_len is not None:
            return min(int(self.max_code_len), max_available)
        return max_available

    def _should_run_fixed_prompt_eval(self):
        if self.trainer.sanity_checking or self.fixed_prompt_eval_samples <= 0 or not self.validation_samples:
            return False
        if not self.trainer.is_global_zero:
            return False
        if self.fixed_prompt_eval_every_n_epochs > 0:
            epoch_idx = int(self.current_epoch)
            epoch_number = epoch_idx + 1
            if epoch_number % self.fixed_prompt_eval_every_n_epochs != 0:
                return False
            if self._last_fixed_prompt_eval_epoch == epoch_idx:
                return False
            self._last_fixed_prompt_eval_epoch = epoch_idx
            return True
        if self.ast_every_n_steps > 0:
            current_step = int(self.trainer.global_step)
            if self._last_ast_eval_step is not None and current_step - self._last_ast_eval_step < self.ast_every_n_steps:
                return False
            self._last_ast_eval_step = current_step
        return True

    def _evaluate_ast_validation_samples(self):
        if self._should_run_fixed_prompt_eval():
            samples = self.validation_samples[: self.ast_eval_samples] # Fix: Use ast_eval_samples (Cause 14)
            generated_texts = []
            target_texts = []
            unresolved_counts = []
            remasked_per_step = []
            eos_hits = []
            generated_lengths = []
            adjacent_repeat_fractions = []
            self.model.eval()

            for sample in samples:
                prompt = sample.get("instruction", "")
                target_code = sample.get("code", "")
                target_texts.append(target_code)
                prompt_ids = self.tokenizer.encode_instruction(prompt)
                if self.max_prompt_len is not None:
                    prompt_ids = pad_or_truncate_ids(prompt_ids, self.max_prompt_len, self.tokenizer.pad_token_id)
                prompt_ids = torch.tensor(prompt_ids, dtype=torch.long, device=self.device).unsqueeze(0)
                target_code_len = len(self.tokenizer.encode_code(target_code))
                if self.max_code_len is not None:
                    target_code_len = min(target_code_len, self.max_code_len)
                generation_code_len = self._fixed_generation_length(
                    prompt_ids.size(1),
                    target_code_len=target_code_len,
                )
                try:
                    gen_ids, telemetry = self.model.generate(
                        prompt_ids,
                        steps=self.ast_generation_steps,
                        device=self.device,
                        eos_token_id=self.tokenizer.code_eos_token_id,
                        code_len=generation_code_len,
                        forbidden_token_ids=self.tokenizer.special_token_ids,
                        return_telemetry=True,
                        **self.generation_config,
                    )
                    token_ids = gen_ids[0].detach().cpu().tolist()
                    code_eos_id = self.tokenizer.code_eos_token_id
                    eos_hit = code_eos_id in token_ids
                    eos_hits.append(float(eos_hit))
                    if eos_hit:
                        generated_length = token_ids.index(code_eos_id) + 1
                    else:
                        generated_length = len(token_ids)
                    generated_lengths.append(float(generated_length))
                    adjacent_repeat_fractions.append(adjacent_repeat_fraction(token_ids[:generated_length]))
                    generated_texts.append(self.tokenizer.decode(token_ids, skip_special_tokens=True))
                    unresolved_counts.append(float(telemetry.get("final_unresolved_mask_count", 0)))
                    remasked = telemetry.get("remasked_tokens") or []
                    if remasked:
                        remasked_per_step.append(sum(remasked) / max(len(remasked), 1))
                except Exception as exc:
                    generated_texts.append("<GENERATION_FAILED>")
                    unresolved_counts.append(0.0)
                    eos_hits.append(0.0)
                    generated_lengths.append(0.0)
                    adjacent_repeat_fractions.append(0.0)
                    if len(generated_texts) <= self.ast_log_failures:
                        print(f"[AST EVAL WARNING] generation failed: {type(exc).__name__}: {exc}")

            result = ast_validity_rate(generated_texts, max_failures=self.ast_log_failures)
            compile_result = compile_validity_rate(generated_texts, max_failures=self.ast_log_failures)
            compile_missing = compile_result.total_count - compile_result.valid_count
            edit_distances = [
                levenshtein_distance(generated, target)
                for generated, target in zip(generated_texts, target_texts)
            ]
            normalized_edit_distances = [
                normalized_levenshtein_distance(generated, target)
                for generated, target in zip(generated_texts, target_texts)
            ]
            
            # Save newly computed metrics to cache (Cause 15)
            self._last_ast_eval_metrics = {
                "val_ast_valid_rate": float(result.rate),
                "val_compile_valid_rate": float(compile_result.rate),
                "val_fixed_prompt_ast_valid_rate": float(result.rate),
                "val_fixed_prompt_compile_valid_rate": float(compile_result.rate),
                "val_fixed_prompt_compile_missing_count": float(compile_missing),
            }
            if edit_distances:
                self._last_ast_eval_metrics["val_fixed_prompt_levenshtein"] = sum(edit_distances) / len(edit_distances)
            if normalized_edit_distances:
                self._last_ast_eval_metrics["val_fixed_prompt_levenshtein_norm"] = sum(normalized_edit_distances) / len(normalized_edit_distances)
            if unresolved_counts:
                self._last_ast_eval_metrics["val_generation_final_unresolved_token_count"] = sum(unresolved_counts) / len(unresolved_counts)
            if remasked_per_step:
                self._last_ast_eval_metrics["val_generation_remasked_tokens_per_step"] = sum(remasked_per_step) / len(remasked_per_step)
            if eos_hits:
                self._last_ast_eval_metrics["val_generation_eos_rate"] = sum(eos_hits) / len(eos_hits)
            if generated_lengths:
                self._last_ast_eval_metrics["val_generation_avg_length"] = sum(generated_lengths) / len(generated_lengths)
            if adjacent_repeat_fractions:
                self._last_ast_eval_metrics["val_generation_adjacent_repeat_fraction"] = sum(adjacent_repeat_fractions) / len(adjacent_repeat_fractions)

            # Console diagnostic output
            for failure in result.failures:
                print(f"[AST INVALID] {failure}")
            for failure in compile_result.failures:
                print(f"[COMPILE INVALID] {failure}")
            if edit_distances:
                print(
                    f"[FIXED PROMPT EVAL] epoch={self.current_epoch + 1} "
                    f"samples={len(generated_texts)} compile_missing={compile_missing}/{compile_result.total_count} "
                    f"levenshtein={sum(edit_distances) / len(edit_distances):.1f} "
                    f"levenshtein_norm={sum(normalized_edit_distances) / len(normalized_edit_distances):.3f}"
                )

        # Log metrics (newly computed or cached from a previous validation run) (Cause 15)
        if self._last_ast_eval_metrics is not None:
            for name, val in self._last_ast_eval_metrics.items():
                self.log(name, torch.tensor(val, device=self.device), sync_dist=False)

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(self.parameters(), lr=self.base_lr, weight_decay=self.weight_decay)
        total_steps = int(getattr(self.trainer, "estimated_stepping_batches", 0) or 1)
        warmup_steps = max(int(self.lr_warmup_steps), 0)
        min_lr_ratio = self.min_lr / self.base_lr if self.base_lr > 0 else 0.0

        def lr_lambda(step):
            step = int(step)
            if warmup_steps > 0 and step < warmup_steps:
                return max((step + 1) / warmup_steps, min_lr_ratio)
            decay_steps = max(total_steps - warmup_steps, 1)
            progress = min(max((step - warmup_steps) / decay_steps, 0.0), 1.0)
            cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
            return min_lr_ratio + (1.0 - min_lr_ratio) * cosine

        scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=lr_lambda)
        return {
            "optimizer": optimizer,
            "lr_scheduler": {
                "scheduler": scheduler,
                "interval": "step",
                "frequency": 1,
            },
        }

    def on_load_checkpoint(self, checkpoint):
        state_dict = checkpoint.get("state_dict") or {}
        state_dict.pop("loss_fn.embedding_matrix", None)
        if self.use_ast_loss and hasattr(self, "ast_embedding") and "ast_embedding.weight" not in state_dict:
            state_dict["ast_embedding.weight"] = self.ast_embedding.weight.detach().clone()
            checkpoint.pop("optimizer_states", None)
            checkpoint.pop("lr_schedulers", None)
            print(
                "[RESUME WARNING] Checkpoint has no ast_embedding.weight; "
                "initialized AST embedding from the current model and skipped optimizer/scheduler restore."
            )
        if not self.use_ast_loss:
            ast_keys = [key for key in state_dict if key.startswith("ast_embedding.")]
            for key in ast_keys:
                state_dict.pop(key, None)
        legacy_keys = {"curriculum_stage", "curriculum_lb", "curriculum_ub"}
        if legacy_keys.intersection(checkpoint):
            print("[RESUME] Ignoring legacy curriculum state; stationary mixed masking is active.")
        if self.rollback_stage is not None:
            print("[RESUME WARNING] ROLLBACK_STAGE is ignored by stationary mixed masking.")


class DiffCoderTrainer:
    def __init__(self, config):
        self.config = config
        self.tokenizer = CodeTokenizer()
        self.setup_data()
        self.setup_model()

    @staticmethod
    def _normalized_val_check_interval(requested_interval, train_batches):
        requested_interval = int(requested_interval)
        train_batches = max(int(train_batches), 1)
        if requested_interval <= 0:
            return 1
        return min(requested_interval, train_batches)

    def setup_data(self):
        repo_root = Path(__file__).resolve().parent.parent
        dataset_path = repo_root / "data" / "dataset.csv"


        cache_root = repo_root / "data" / "tokenized_cache"
        cache_dir = tokenized_cache_dir(
            cache_root=cache_root,
            tokenizer_name=self.tokenizer.model_name,
            max_prompt_len=self.config.max_prompt_len,
            max_code_len=self.config.max_code_len,
            pad_token_id=self.tokenizer.pad_token_id,
            vocab_size=self.tokenizer.vocab_size,
            dataset_fraction=self.config.dataset_fraction,
            max_ast_len=self.config.max_ast_len,
            require_valid=self.config.dataset_require_valid,
            compile_filter=self.config.dataset_compile_filter,
            canonicalize_instructions=self.config.dataset_canonicalize_instructions,
        )
        cache_dir = ensure_tokenized_cache(
            csv_path=dataset_path,
            tokenizer=self.tokenizer,
            cache_dir=cache_dir,
            max_prompt_len=self.config.max_prompt_len,
            max_code_len=self.config.max_code_len,
            max_ast_len=self.config.max_ast_len,
            dataset_fraction=self.config.dataset_fraction,
            chunk_size=self.config.cache_chunk_size,
            encode_batch_size=self.config.encode_batch_size,
            force_rebuild=self.config.rebuild_token_cache,
            require_valid=self.config.dataset_require_valid,
            compile_filter=self.config.dataset_compile_filter,
            canonicalize_instructions=self.config.dataset_canonicalize_instructions,
            sample_count=self.config.fixed_prompt_eval_samples,
        )
        self.cache_dir = cache_dir

        full_dataset = TokenizedMemmapDataset(cache_dir)
        train_indices, val_indices = make_train_val_indices(
            len(full_dataset),
            val_split=self.config.val_split,
            max_val_samples=self.config.max_val_samples,
            seed=42,
            group_ids=full_dataset.group_ids, # Group-based splitting (Cause 7)
        )

        self.train_dataset = TokenizedMemmapDataset(cache_dir, train_indices)
        self.val_dataset = TokenizedMemmapDataset(cache_dir, val_indices)
        print(
            f"[DATA] Train rows: {len(self.train_dataset):,} | "
            f"validation rows: {len(self.val_dataset):,}"
        )

        loader_kwargs = {
            "num_workers": self.config.num_workers,
            "pin_memory": torch.cuda.is_available(),
            "collate_fn": collate_tokenized_batch,
        }
        if self.config.num_workers > 0:
            loader_kwargs["persistent_workers"] = True
            loader_kwargs["prefetch_factor"] = self.config.prefetch_factor

        self.train_loader = DataLoader(
            self.train_dataset, batch_size=self.config.batch_size, shuffle=True,
            drop_last=True,
            **loader_kwargs
        )
        self.val_loader = DataLoader(
            self.val_dataset, batch_size=self.config.batch_size, shuffle=False,
            **loader_kwargs
        )

        # Select validation-only samples to avoid training leakage and out-of-bounds indexing (Cause 8)
        self.sample_pairs = []
        if len(self.val_dataset) > 0:
            num_eval_samples = min(int(self.config.fixed_prompt_eval_samples), len(self.val_dataset))
            for idx in range(num_eval_samples):
                row = self.val_dataset[idx]
                row_idx = int(self.val_dataset.indices[idx]) if self.val_dataset.indices is not None else int(idx)
                prompt_len = int(self.val_dataset.prompt_lens[row_idx])
                code_len = int(self.val_dataset.code_lens[row_idx])
                
                # Retrieve the sliced tokens (non-padded part)
                p_ids = row["prompt_ids"][:prompt_len]
                c_ids = row["code_ids"][:code_len]
                
                instruction = self.tokenizer.decode(p_ids, skip_special_tokens=True)
                code = self.tokenizer.decode(c_ids, skip_special_tokens=True)
                self.sample_pairs.append({
                    "instruction": instruction,
                    "code": code
                })

    def setup_model(self):
        raw_model = LocalConvDiffCoder(
            vocab_size=self.tokenizer.vocab_size,
            mask_token_id=self.tokenizer.mask_token_id,
            pad_token_id=self.tokenizer.pad_token_id,
            hidden_dim=self.config.hidden_dim,
            num_blocks=self.config.num_blocks,
            max_seq_len=self.config.max_prompt_len + self.config.max_code_len,
            dilation_factor=self.config.dilation_factor,
            dropout=self.config.dropout,
        )
        
        mask_sampler = MixtureMaskSampler(self.config.mask_sampler_config)
        corruptor = CodeCorruptor(
            mask_token_id=self.tokenizer.mask_token_id,
            pad_token_id=self.tokenizer.pad_token_id,
            protected_token_ids=self.tokenizer.corruption_protected_token_ids,
            config=self.config.topology_config,
        )

        self.lightning_model = MixedDiffCoderLightning(
            model=raw_model,
            tokenizer=self.tokenizer,
            mask_sampler=mask_sampler,
            corruptor=corruptor,
            validation_mask_bins=self.config.validation_mask_bins,
            validation_seed=self.config.validation_seed,
            validation_samples=self.sample_pairs,
            fixed_prompt_eval_samples=self.config.fixed_prompt_eval_samples,
            fixed_prompt_eval_every_n_epochs=self.config.fixed_prompt_eval_every_n_epochs,
            fixed_generation_code_len=self.config.fixed_generation_code_len,
            ast_eval_samples=self.config.ast_eval_samples,
            ast_generation_steps=self.config.ast_generation_steps,
            ast_every_n_steps=self.config.ast_every_n_steps,
            ast_log_failures=self.config.ast_log_failures,
            generation_config=self.config.generation_config,
            validation_logit_chunk_size=self.config.validation_logit_chunk_size,
            mask_telemetry_every_n_steps=self.config.mask_telemetry_every_n_steps,
            max_prompt_len=self.config.max_prompt_len,
            max_code_len=self.config.max_code_len,
            prompt_shuffle_diagnostic=self.config.prompt_shuffle_diagnostic,
            prompt_shuffle_mask_prob=self.config.prompt_shuffle_mask_prob,
            reference_cache_dir=self.cache_dir,
            multi_reference_loss=self.config.multi_reference_loss,
            multi_reference_max_refs=self.config.multi_reference_max_refs,
            train_logit_chunk_size=self.config.train_logit_chunk_size,
            lr_warmup_steps=self.config.lr_warmup_steps,
            min_lr=self.config.min_lr,
            base_lr=self.config.base_lr,
            weight_decay=self.config.weight_decay,
            rollback_stage=self.config.rollback_stage,
            use_ast_loss=self.config.use_ast_loss,
            ast_loss_base_weight=self.config.ast_loss_base_weight,
            ast_loss_scale=self.config.ast_loss_scale,
            max_ast_len=self.config.max_ast_len,
            ast_dtw_max_code_len=self.config.ast_dtw_max_code_len,
            ast_dtw_max_ast_len=self.config.ast_dtw_max_ast_len,
            ast_loss_every_n_steps=self.config.ast_loss_every_n_steps,
            ast_loss_probability=self.config.ast_loss_probability,
            prompt_contrastive_loss=self.config.prompt_contrastive_loss,
            prompt_contrastive_weight=self.config.prompt_contrastive_weight,
            prompt_contrastive_margin=self.config.prompt_contrastive_margin,
            prompt_contrastive_mask_prob=self.config.prompt_contrastive_mask_prob,
            focal_loss_gamma=self.config.focal_loss_gamma,
            batch_token_weighting=self.config.batch_token_weighting,
            batch_token_weight_min=self.config.batch_token_weight_min,
            batch_token_weight_max=self.config.batch_token_weight_max,
        )

    def train(self):
        resume_checkpoint_path = self._resolve_resume_checkpoint_path()

        best_checkpoint_callback = ModelCheckpoint(
            monitor=self.config.checkpoint_monitor,
            dirpath=self.config.checkpoint_dir,
            filename='diffcoder-{epoch:02d}-{val_loss:.4f}',
            save_top_k=1,
            mode=self.config.checkpoint_mode,
        )

        last_checkpoint_callback = ModelCheckpoint(
            dirpath=self.config.checkpoint_dir,
            filename='last', 
            save_top_k=0,
            save_last=True,
            every_n_train_steps=self.config.checkpoint_every_n_steps,
            save_on_train_epoch_end=False,
            enable_version_counter=False,
        )

        early_stop_callback = EarlyStopping(
            monitor=self.config.early_stopping_monitor,
            patience=self.config.early_stopping_patience,
            mode=self.config.early_stopping_mode,
            verbose=True
        )
        
        lr_monitor = LearningRateMonitor(logging_interval='epoch')
        sample_logger_callback = LogGeneratedSamplesCallback(
            sample_pairs=self.sample_pairs,
            tokenizer=self.tokenizer,
            every_n_steps=self.config.sample_log_every_n_steps,
            console_chars=self.config.sample_console_chars,
            generation_steps=self.config.sample_generation_steps,
            max_prompt_len=self.config.max_prompt_len,
            max_code_len=self.config.max_code_len,
        )
        throughput_logger_callback = ThroughputLoggerCallback(
            every_n_batches=self.config.console_log_every_n_batches
        )
        reset_early_stop_callback = ResetEarlyStoppingOnResumeCallback(
            enabled=bool(resume_checkpoint_path and self.config.reset_early_stopping_on_resume)
        )

        loggers = []
        comet_logger = None
        datehourstr = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if os.getenv("COMET_API_KEY"):
            comet_experiment_key = (os.getenv("COMET_EXPERIMENT_KEY") or "").strip() or None
            comet_mode = (os.getenv("COMET_MODE") or "").strip() or None
            if comet_experiment_key:
                comet_mode = comet_mode or "get_or_create"
            else:
                os.environ.pop("COMET_EXPERIMENT_KEY", None)
                if not comet_mode:
                    os.environ.pop("COMET_MODE", None)
                if comet_mode in {"get", "get_or_create"}:
                    print(f"[COMET WARNING] COMET_MODE={comet_mode!r} requires COMET_EXPERIMENT_KEY. Using 'create'.")
                comet_mode = "create"
            comet_logger = CometLogger(
                api_key=os.getenv("COMET_API_KEY"),
                project=os.getenv("COMET_PROJECT_NAME"),
                workspace=os.getenv("COMET_WORKSPACE"),
                experiment_key=comet_experiment_key,
                mode=comet_mode,
                name=os.getenv("COMET_EXPERIMENT_NAME", f"diffcoder-light-train-{datehourstr}"),
            )
            loggers.append(comet_logger)

        callbacks = [
            best_checkpoint_callback,
            last_checkpoint_callback,
            early_stop_callback,
            lr_monitor,
            throughput_logger_callback,
            sample_logger_callback,
            reset_early_stop_callback,
        ]

        if self.config.upload_checkpoints_to_comet:
            callbacks.append(
                CometCheckpointUploadCallback(
                    best_checkpoint_callback=best_checkpoint_callback,
                    last_checkpoint_callback=last_checkpoint_callback,
                    mode=self.config.checkpoint_mode,
                )
            )

        train_batches = max(len(self.train_loader), 1)
        normalized_val_check_interval = self._normalized_val_check_interval(
            self.config.val_check_interval,
            train_batches,
        )
        if normalized_val_check_interval != int(self.config.val_check_interval):
            print(
                f"[CONFIG WARNING] VAL_CHECK_INTERVAL={self.config.val_check_interval} exceeds "
                f"train batches ({train_batches}); using {normalized_val_check_interval} instead."
            )

        trainer = pl.Trainer(
            max_epochs=self.config.epochs,
            max_steps=self.config.max_steps,
            accelerator='gpu' if torch.cuda.is_available() else 'cpu',
            devices=1 if torch.cuda.is_available() else "auto",
            accumulate_grad_batches=self.config.accumulation_steps,
            callbacks=callbacks,
            logger=loggers if loggers else True,
            precision="16-mixed" if torch.cuda.is_available() else 32,
            gradient_clip_val=1.0,
            val_check_interval=normalized_val_check_interval,
            limit_val_batches=self.config.limit_val_batches,
            log_every_n_steps=self.config.log_every_n_steps,
            num_sanity_val_steps=self.config.num_sanity_val_steps,
        )

        trainer.fit(
            self.lightning_model, 
            train_dataloaders=self.train_loader, 
            val_dataloaders=self.val_loader,
            ckpt_path=resume_checkpoint_path,
        )

        def scalar_metric(name):
            value = trainer.callback_metrics.get(name)
            if value is None:
                return None
            if hasattr(value, "detach"):
                value = value.detach().cpu()
            if hasattr(value, "item"):
                return float(value.item())
            return float(value)

        best_score = best_checkpoint_callback.best_model_score
        best_monitor_score = None
        if best_score is not None:
            best_monitor_score = float(best_score.detach().cpu().item() if hasattr(best_score, "detach") else best_score)

        last_model_path = getattr(last_checkpoint_callback, "last_model_path", "") or last_checkpoint_callback.best_model_path
        train_result = {
            "best_monitor": self.config.checkpoint_monitor,
            "best_monitor_score": best_monitor_score,
            "final_val_loss": scalar_metric("val_loss"),
            "final_checkpoint_monitor": scalar_metric(self.config.checkpoint_monitor),
            "final_train_loss": scalar_metric("train_loss"),
            "best_model_path": best_checkpoint_callback.best_model_path,
            "last_model_path": last_model_path,
            "global_step": int(trainer.global_step),
            "current_epoch": int(trainer.current_epoch),
            "train_rows": len(self.train_dataset),
            "val_rows": len(self.val_dataset),
            "resume_checkpoint_path": resume_checkpoint_path,
            "config": {
                "batch_size": self.config.batch_size,
                "accumulation_steps": self.config.accumulation_steps,
                "base_lr": self.config.base_lr,
                "weight_decay": self.config.weight_decay,
                "hidden_dim": self.config.hidden_dim,
                "num_blocks": self.config.num_blocks,
                "dilation_factor": self.config.dilation_factor,
                "max_prompt_len": self.config.max_prompt_len,
                "max_code_len": self.config.max_code_len,
                "max_steps": self.config.max_steps,
                "dropout": self.config.dropout,
                "code_eos_token_id": self.tokenizer.code_eos_token_id,
                "dataset_require_valid": self.config.dataset_require_valid,
                "dataset_compile_filter": self.config.dataset_compile_filter,
                "dataset_canonicalize_instructions": self.config.dataset_canonicalize_instructions,
                "multi_reference_loss": self.config.multi_reference_loss,
                "multi_reference_max_refs": self.config.multi_reference_max_refs,
                "train_logit_chunk_size": self.config.train_logit_chunk_size,
                "checkpoint_monitor": self.config.checkpoint_monitor,
                "checkpoint_mode": self.config.checkpoint_mode,
                "reset_early_stopping_on_resume": self.config.reset_early_stopping_on_resume,
                "lr_warmup_steps": self.config.lr_warmup_steps,
                "min_lr": self.config.min_lr,
                "masking": {
                    "sampler": [
                        {
                            "name": regime.name,
                            "range": [regime.low, regime.high],
                            "weight": regime.weight,
                            "alpha": regime.alpha,
                            "beta": regime.beta,
                        }
                        for regime in self.config.mask_sampler_config.regimes
                    ],
                    "topology": {
                        "independent": self.config.topology_config.independent,
                        "block": self.config.topology_config.block,
                        "prefix": self.config.topology_config.prefix,
                        "truncated_suffix": self.config.topology_config.truncated_suffix,
                        "block_lengths": list(self.config.topology_config.block_lengths),
                    },
                },
                "validation": {
                    "fixed_mask_bins": list(self.config.validation_mask_bins),
                    "deterministic_seed": self.config.validation_seed,
                    "fixed_prompt_eval_samples": self.config.fixed_prompt_eval_samples,
                    "fixed_prompt_eval_every_n_epochs": self.config.fixed_prompt_eval_every_n_epochs,
                    "fixed_generation_code_len": self.config.fixed_generation_code_len,
                    "ast_eval_samples": self.config.ast_eval_samples,
                    "prompt_shuffle_diagnostic": self.config.prompt_shuffle_diagnostic,
                    "prompt_shuffle_mask_prob": self.config.prompt_shuffle_mask_prob,
                },
                "generation": self.config.generation_config,
            },
        }

        result_json = os.getenv("TRAIN_RESULT_JSON")
        if result_json:
            result_path = Path(result_json)
            result_path.parent.mkdir(parents=True, exist_ok=True)
            result_path.write_text(json.dumps(train_result, ensure_ascii=True, indent=2), encoding="utf-8")
        
        if self.config.upload_checkpoints_to_comet and comet_logger is not None and best_checkpoint_callback.best_model_path:
            try:
                comet_logger.experiment.log_model(
                    "LocalConvDiffCoder-best",
                    best_checkpoint_callback.best_model_path,
                    overwrite=True,
                )
            except Exception as e:
                print(f"[COMET WARNING] Nie udało się automatycznie zalogować BEST modelu: {e}")

        if self.config.upload_checkpoints_to_comet and comet_logger is not None and last_model_path:
            try:
                comet_logger.experiment.log_model(
                    "LocalConvDiffCoder-last",
                    last_model_path,
                    overwrite=True,
                )
            except Exception as e:
                print(f"[COMET WARNING] Nie udało się automatycznie zalogować LAST modelu: {e}")

        return train_result

    def _resolve_resume_checkpoint_path(self):
        explicit = str(getattr(self.config, "resume_checkpoint_path", "") or "").strip()
        if explicit:
            path = Path(explicit)
            if not path.is_absolute():
                path = Path(__file__).resolve().parent.parent / path
            path = path.resolve()
            if not path.is_file():
                raise FileNotFoundError(f"RESUME_CHECKPOINT_PATH does not exist: {path}")
            print(f"[RESUME] Loading checkpoint: {path}")
            return str(path)

        if not getattr(self.config, "auto_resume_last", False):
            return None

        checkpoint_dir = Path(self.config.checkpoint_dir)
        if not checkpoint_dir.is_absolute():
            checkpoint_dir = Path(__file__).resolve().parent.parent / checkpoint_dir
        last_path = (checkpoint_dir / "last.ckpt").resolve()
        if last_path.is_file():
            print(f"[RESUME] Auto-resuming from last checkpoint: {last_path}")
            return str(last_path)

        print(f"[RESUME] AUTO_RESUME_LAST=1 but no last.ckpt found in {checkpoint_dir}. Starting fresh.")
        return None

def env_bool(name, default=False):
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def env_float(name, default):
    return float(os.getenv(name, str(default)))


def env_int(name, default):
    return int(os.getenv(name, str(default)))


def env_float_list(name, default):
    value = os.getenv(name)
    if value is None:
        value = default
    if isinstance(value, (list, tuple)):
        return [float(item) for item in value]
    return [float(part.strip()) for part in str(value).split(",") if part.strip()]


def env_int_list(name, default):
    value = os.getenv(name)
    if value is None:
        value = default
    if isinstance(value, (list, tuple)):
        return [int(item) for item in value]
    return [int(part.strip()) for part in str(value).split(",") if part.strip()]


def env_float_pair(name, default):
    values = env_float_list(name, default)
    if len(values) != 2:
        raise ValueError(f"{name} must contain exactly two comma-separated floats.")
    return values[0], values[1]


def warn_mask_range_gaps(regimes):
    sorted_regimes = sorted(regimes, key=lambda regime: regime.low)
    previous_high = sorted_regimes[0].high if sorted_regimes else 0.0
    for regime in sorted_regimes[1:]:
        is_exact_all = abs(regime.low - 1.0) <= 1e-6 and abs(regime.high - 1.0) <= 1e-6
        if is_exact_all and previous_high >= 0.95:
            previous_high = max(previous_high, regime.high)
            continue
        if regime.low > previous_high + 1e-6:
            print(
                f"[MASK WARNING] Training mask ranges leave a gap "
                f"{previous_high:.2f}-{regime.low:.2f} before regime {regime.name!r}."
            )
        previous_high = max(previous_high, regime.high)


def main():
    torch.backends.cudnn.enabled = True
    env_test_path = Path(__file__).resolve().parent.parent / ".env.test"
    
    # is_testing = (
    #     os.getenv("USE_TEST_ENV") == "1"
    #     or os.getenv("DIFFCODER_TEST") == "1"
    #     or os.getenv("PYTEST_CURRENT_TEST") is not None
    #     or "pytest" in sys.modules
    #     or "unittest" in sys.modules
    # )
    is_testing = False
    if is_testing and env_test_path.exists():
        load_dotenv(dotenv_path=env_test_path, override=True)
    else:
        load_dotenv()

    # Reproducibility configurations (Cause 21)
    global_seed_val = os.getenv("GLOBAL_SEED")
    global_seed = int(global_seed_val) if global_seed_val else 42
    pl.seed_everything(global_seed, workers=True)
    
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True
        torch.backends.cudnn.deterministic = False
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True
        torch.set_float32_matmul_precision("high")

    class Config:
        max_prompt_len = int(os.getenv("MAX_PROMPT_LEN", "96"))
        max_code_len = int(os.getenv("MAX_CODE_LEN", "512"))
        batch_size = int(os.getenv("BATCH_SIZE", "32"))
        accumulation_steps = int(os.getenv("ACCUMULATION_STEPS", "1"))
        num_workers = int(os.getenv("NUM_WORKERS", "6"))
        prefetch_factor = int(os.getenv("PREFETCH_FACTOR", "4"))
        epochs = 1500 
        max_steps = int(os.getenv("MAX_STEPS", "-1"))
        val_split = float(os.getenv("VAL_SPLIT", "0.01"))
        max_val_samples = int(os.getenv("MAX_VAL_SAMPLES", "8192"))
        limit_val_batches = int(os.getenv("LIMIT_VAL_BATCHES", "128"))
        val_check_interval = int(os.getenv("VAL_CHECK_INTERVAL", "1000"))
        checkpoint_every_n_steps = int(os.getenv("CHECKPOINT_EVERY_N_STEPS", "1000"))
        log_every_n_steps = int(os.getenv("LOG_EVERY_N_STEPS", "25"))
        console_log_every_n_batches = int(os.getenv("CONSOLE_LOG_EVERY_N_BATCHES", "250"))
        mask_telemetry_every_n_steps = int(os.getenv("MASK_TELEMETRY_EVERY_N_STEPS", "50"))
        sample_log_every_n_steps = int(os.getenv("SAMPLE_LOG_EVERY_N_STEPS", "1000"))
        sample_console_chars = int(os.getenv("SAMPLE_CONSOLE_CHARS", "1200"))
        sample_generation_steps = int(os.getenv("SAMPLE_GENERATION_STEPS", "50"))
        num_sanity_val_steps = int(os.getenv("NUM_SANITY_VAL_STEPS", "0"))
        early_stopping_patience = 15
        hidden_dim = int(os.getenv("HIDDEN_DIM", "512"))
        num_blocks = int(os.getenv("NUM_BLOCKS", "6"))
        dilation_factor = int(os.getenv("DILATION_FACTOR", "2"))
        dataset_fraction = float(os.getenv("DATASET_FRACTION", "1.0"))
        dataset_require_valid = env_bool("DATASET_REQUIRE_VALID", True)
        dataset_compile_filter = os.getenv("DATASET_COMPILE_FILTER", "exclude_false").strip().lower()
        dataset_canonicalize_instructions = env_bool("DATASET_CANONICALIZE_INSTRUCTIONS", False)
        multi_reference_loss = env_bool("MULTI_REFERENCE_LOSS", False)
        multi_reference_max_refs = env_int("MULTI_REFERENCE_MAX_REFS", 32)
        train_logit_chunk_size = env_int("TRAIN_LOGIT_CHUNK_SIZE", 2048)
        dropout = env_float("DROPOUT", 0.1)
        cache_chunk_size = int(os.getenv("CACHE_CHUNK_SIZE", "8192"))
        encode_batch_size = int(os.getenv("ENCODE_BATCH_SIZE", "512"))
        rebuild_token_cache = env_bool("REBUILD_TOKEN_CACHE", False)
        use_ast_loss = env_bool("USE_AST_LOSS", False)
        max_ast_len = int(os.getenv("MAX_AST_LEN", "256"))
        ast_dtw_max_code_len = env_int("AST_DTW_MAX_CODE_LEN", 64)
        ast_dtw_max_ast_len = env_int("AST_DTW_MAX_AST_LEN", 64)
        ast_loss_every_n_steps = env_int("AST_LOSS_EVERY_N_STEPS", 1)
        ast_loss_probability = env_float("AST_LOSS_PROBABILITY", 1.0)
        ast_loss_base_weight = float(os.getenv("AST_LOSS_BASE_WEIGHT", "0.1"))
        ast_loss_scale = float(os.getenv("AST_LOSS_SCALE", "0.4"))
        prompt_contrastive_loss = env_bool("PROMPT_CONTRASTIVE_LOSS", True)
        prompt_contrastive_weight = env_float("PROMPT_CONTRASTIVE_WEIGHT", 0.25)
        prompt_contrastive_margin = env_float("PROMPT_CONTRASTIVE_MARGIN", 0.25)
        prompt_contrastive_mask_prob = env_float("PROMPT_CONTRASTIVE_MASK_PROB", 1.0)
        focal_loss_gamma = env_float("FOCAL_LOSS_GAMMA", 1.5)
        batch_token_weighting = env_bool("BATCH_TOKEN_WEIGHTING", True)
        batch_token_weight_min = env_float("BATCH_TOKEN_WEIGHT_MIN", 0.25)
        batch_token_weight_max = env_float("BATCH_TOKEN_WEIGHT_MAX", 4.0)
        upload_checkpoints_to_comet = env_bool("COMET_UPLOAD_CHECKPOINTS", False)
        base_lr = float(os.getenv("BASE_LR", "5e-5"))
        min_lr = env_float("MIN_LR", 1e-6)
        lr_warmup_steps = env_int("LR_WARMUP_STEPS", 1000)
        weight_decay = float(os.getenv("WEIGHT_DECAY", "0.01"))
        
        checkpoint_dir = os.getenv("CHECKPOINT_DIR", str(Path(__file__).resolve().parent.parent / "checkpoints"))
        default_cp_monitor = "val_total_loss" if use_ast_loss else "val_loss"
        checkpoint_monitor = os.getenv("CHECKPOINT_MONITOR", default_cp_monitor)
        
        default_cp_mode = "max" if ("valid" in checkpoint_monitor or "accuracy" in checkpoint_monitor or "rate" in checkpoint_monitor) else "min"
        checkpoint_mode = os.getenv("CHECKPOINT_MODE", default_cp_mode)
        resume_checkpoint_path = os.getenv("RESUME_CHECKPOINT_PATH", "")
        auto_resume_last = env_bool("AUTO_RESUME_LAST", False)
        reset_early_stopping_on_resume = env_bool("RESET_EARLY_STOPPING_ON_RESUME", True)
        
        # Early stopping configurations
        global_seed = env_int("GLOBAL_SEED", 42)
        default_es_monitor = "val_total_loss" if env_bool("USE_AST_LOSS", False) else "val_loss"
        early_stopping_monitor = os.getenv("EARLY_STOPPING_MONITOR", default_es_monitor)
        default_es_mode = "max" if ("valid" in early_stopping_monitor or "accuracy" in early_stopping_monitor or "rate" in early_stopping_monitor) else "min"
        early_stopping_mode = os.getenv("EARLY_STOPPING_MODE", default_es_mode)
        
        # Legacy curriculum overrides are ignored by MixedDiffCoderLightning.
        rollback_stage = int(os.getenv("ROLLBACK_STAGE")) if os.getenv("ROLLBACK_STAGE") else None

        mask_low_range = env_float_pair("MASK_LOW_RANGE", "0.05,0.35")
        mask_middle_range = env_float_pair("MASK_MIDDLE_RANGE", "0.35,0.70")
        mask_high_range = env_float_pair("MASK_HIGH_RANGE", "0.70,0.95")
        mask_sampler_seed = int(os.getenv("MASK_SAMPLER_SEED")) if os.getenv("MASK_SAMPLER_SEED") else None
        mask_low_weight = env_float("MASK_LOW_WEIGHT", 0.05)
        mask_middle_weight = env_float("MASK_MIDDLE_WEIGHT", 0.15)
        mask_high_weight = env_float("MASK_HIGH_WEIGHT", 0.20)
        if os.getenv("MASK_ALL_WEIGHT") is None:
            mask_all_weight = 0.60
            other_weight = mask_low_weight + mask_middle_weight + mask_high_weight
            if other_weight > 0:
                scale = (1.0 - mask_all_weight) / other_weight
                mask_low_weight *= scale
                mask_middle_weight *= scale
                mask_high_weight *= scale
        else:
            mask_all_weight = env_float("MASK_ALL_WEIGHT", 0.60)
        mask_sampler_config = MixtureMaskSamplerConfig(
            regimes=(
                NoiseRegimeConfig(
                    name="low",
                    low=mask_low_range[0],
                    high=mask_low_range[1],
                    weight=mask_low_weight,
                    alpha=env_float("MASK_LOW_ALPHA", 1.2),
                    beta=env_float("MASK_LOW_BETA", 1.2),
                ),
                NoiseRegimeConfig(
                    name="middle",
                    low=mask_middle_range[0],
                    high=mask_middle_range[1],
                    weight=mask_middle_weight,
                    alpha=env_float("MASK_MIDDLE_ALPHA", 2.0),
                    beta=env_float("MASK_MIDDLE_BETA", 2.0),
                ),
                NoiseRegimeConfig(
                    name="high",
                    low=mask_high_range[0],
                    high=mask_high_range[1],
                    weight=mask_high_weight,
                    alpha=env_float("MASK_HIGH_ALPHA", 1.0),
                    beta=env_float("MASK_HIGH_BETA", 1.0),
                ),
                NoiseRegimeConfig(
                    name="all",
                    low=1.0,
                    high=1.0,
                    weight=mask_all_weight,
                    alpha=1.0,
                    beta=1.0,
                ),
            ),
            seed=mask_sampler_seed,
        )
        warn_mask_range_gaps(mask_sampler_config.regimes)
        topology_config = TopologyConfig(
            independent=env_float("TOPOLOGY_INDEPENDENT_WEIGHT", 1.00),
            block=env_float("TOPOLOGY_BLOCK_WEIGHT", 0.00),
            prefix=env_float("TOPOLOGY_PREFIX_WEIGHT", 0.00),
            truncated_suffix=env_float("TOPOLOGY_TRUNCATED_SUFFIX_WEIGHT", 0.00),
            block_lengths=tuple(env_int_list("TOPOLOGY_BLOCK_LENGTHS", "2,4,8")),
            min_visible_prefix_fraction=env_float("TOPOLOGY_MIN_VISIBLE_PREFIX_FRACTION", 0.05),
            max_visible_prefix_fraction=env_float("TOPOLOGY_MAX_VISIBLE_PREFIX_FRACTION", 0.75),
            min_truncated_visible_tokens=env_int("TOPOLOGY_MIN_TRUNCATED_VISIBLE_TOKENS", 1),
            # FIX (Cause 3/4): suppress prefix/suffix topology at high mask ratios
            high_mask_independent_threshold=env_float("TOPOLOGY_HIGH_MASK_INDEPENDENT_THRESHOLD", 0.80),
        )
        validation_mask_bins = tuple(env_float_list("VAL_FIXED_MASK_BINS", "0.25,0.50,0.75,0.95,1.00"))
        validation_seed = env_int("VAL_DETERMINISTIC_SEED", 42)
        validation_logit_chunk_size = env_int("VAL_LOGIT_CHUNK_SIZE", 1024)
        fixed_prompt_eval_samples = env_int("VAL_FIXED_PROMPT_SAMPLES", 5)
        fixed_prompt_eval_every_n_epochs = env_int("VAL_FIXED_PROMPT_EVERY_N_EPOCHS", 1)
        fixed_generation_code_len = env_int("VAL_FIXED_GENERATION_CODE_LEN", 0)
        ast_eval_samples = env_int("VAL_AST_EVAL_SAMPLES", fixed_prompt_eval_samples)
        ast_generation_steps = env_int("VAL_AST_GENERATION_STEPS", 50)
        ast_every_n_steps = env_int("VAL_AST_EVERY_N_STEPS", 0)
        ast_log_failures = env_int("VAL_AST_LOG_FAILURES", 3)
        prompt_shuffle_diagnostic = env_bool("VAL_PROMPT_SHUFFLE_DIAGNOSTIC", True)
        prompt_shuffle_mask_prob = env_float("VAL_PROMPT_SHUFFLE_MASK_PROB", 1.0)
        generation_config = {
            "decoding_strategy": os.getenv("GENERATION_DECODING_STRATEGY", "rcr"),
            "remask_confidence_threshold": env_float("GENERATION_REMASK_CONFIDENCE_THRESHOLD", 0.55),
            "max_remask_fraction_per_step": env_float("GENERATION_MAX_REMASK_FRACTION_PER_STEP", 0.10),
            "max_remasks_per_token": env_int("GENERATION_MAX_REMASKS_PER_TOKEN", 2),
            "remask_cooldown_steps": env_int("GENERATION_REMASK_COOLDOWN_STEPS", 1),
            "disable_remasking_last_n_steps": env_int("GENERATION_DISABLE_REMASKING_LAST_N_STEPS", 2),
            "sampling": env_bool("GENERATION_SAMPLING", False),
        }

    config = Config()
    if not config.use_ast_loss:
        print("[CONFIG WARNING] USE_AST_LOSS=0; DTW/val_dtw_loss and AST training loss are disabled.")
    if config.val_check_interval < 100 or config.sample_log_every_n_steps < 100:
        print(
            "[CONFIG WARNING] Very frequent validation/sample logging is configured; "
            "this can dominate runtime. Prefer VAL_CHECK_INTERVAL>=1000 and SAMPLE_LOG_EVERY_N_STEPS>=5000 for training."
        )
    print(
        "[CONFIG] "
        f"val_check_interval={config.val_check_interval} "
        f"sample_log_every_n_steps={config.sample_log_every_n_steps} "
        f"generation_sampling={config.generation_config.get('sampling')} "
        f"use_ast_loss={config.use_ast_loss} "
        f"ast_dtw_caps={config.ast_dtw_max_code_len}x{config.ast_dtw_max_ast_len}"
    )
    trainer = DiffCoderTrainer(config)
    train_result = trainer.train()
    print(f"\nTrening zakończony. Najlepszy checkpoint: {train_result.get('best_model_path')}")
    print(f"Najlepszy {train_result.get('best_monitor')}: {train_result.get('best_monitor_score')}")


if __name__ == "__main__":
    main()
