from datetime import datetime
from pathlib import Path
import os
import time
import torch
import torch.nn.functional as F
import gc 
from torch.utils.data import DataLoader
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor, EarlyStopping, Callback
from pytorch_lightning.loggers import CometLogger
from dotenv import load_dotenv

# Importy z Twoich modułów
from diffusion.model import LocalConvDiffCoder
from tokenizer import CodeTokenizer 
from diffusion.loss import CalculateLoss
from tokenized_dataset import (
    TokenizedMemmapDataset,
    collate_tokenized_batch,
    ensure_tokenized_cache,
    load_cached_samples,
    make_train_val_indices,
    tokenized_cache_dir,
)

load_dotenv()



def sample_epoch_mask_prob(batch_size, device, lower_bound, upper_bound):
    return lower_bound + torch.rand(batch_size, device=device) * (upper_bound - lower_bound)


# --- LIGHTNING MODULE ---

class DiffCoderLightning(pl.LightningModule):
    def __init__(self, model, base_lr=5e-5, rollback_stage=None, use_ast_loss=False):
        super().__init__()
        self.model = model
        self.base_lr = base_lr
        self.rollback_stage = rollback_stage
        self.use_ast_loss = use_ast_loss
        
        self.current_stage = 1
        self.current_lower_bound = 0.10
        self.current_upper_bound = 0.25
        
        embedding_layer = getattr(model, "token_embedding", getattr(model, "embedding", None)) if use_ast_loss else None
        self.loss_fn = CalculateLoss(
            gamma=1.0,
            ce_weight=1.0,
            dtw_weight=1.0 if use_ast_loss else 0.0,
            embedding_matrix=embedding_layer.weight if embedding_layer is not None else None,
        )

    def _get_ast_embeddings(self, batch):
        if 'ast_vec' not in batch or batch.get('ast_vec') is None:
            return None
        
        ast_vec = batch.get('ast_vec')
        embed_mat = self.loss_fn.embedding_matrix
        if embed_mat is None:
            return None
            
        embed_mat = embed_mat.to(self.device)
        if embed_mat.size(0) >= ast_vec.size(1):
            W = embed_mat[:ast_vec.size(1), :]
        else:
            W = embed_mat.mean(dim=0, keepdim=True).repeat(ast_vec.size(1), 1)
            
        ast_proj = ast_vec @ W
        return ast_proj.unsqueeze(1)

    def _shared_step(self, batch):
        x_0 = batch['code_ids']
        prompt_ids = batch['prompt_ids']
        batch_size, seq_len = x_0.shape

        lb = self.current_lower_bound
        ub = self.current_upper_bound

        mask_prob = sample_epoch_mask_prob(batch_size, self.device, lb, ub)
        mask_prob_expanded = mask_prob.view(batch_size, 1)
        t = mask_prob.view(-1)
        
        rand_matrix = torch.rand(batch_size, seq_len, device=self.device)
        is_masked = (rand_matrix < mask_prob_expanded) & (x_0 != self.model.pad_token_id)
        
        x_t = x_0.clone()
        x_t[is_masked] = self.model.mask_token_id
        
        masked_targets = x_0[is_masked]

        if masked_targets.numel() == 0:
            return torch.tensor(0.0, device=self.device, requires_grad=True)

        if not self.use_ast_loss:
            masked_logits = self.model.forward_masked_logits(x_t, prompt_ids, t, is_masked)
            return F.cross_entropy(masked_logits, masked_targets)

        logits = self.model(x_t, prompt_ids, t)
        masked_logits = logits[is_masked]
        ast_embeddings = self._get_ast_embeddings(batch)

        _, ce_loss, dtw_loss = self.loss_fn(
            full_logits=logits,
            masked_logits=masked_logits,
            masked_targets=masked_targets,
            ast_embeddings=ast_embeddings,
        )

        mean_t = t.mean()
        weighted_dtw = (0.1 + 0.4 * mean_t) * dtw_loss
        return ce_loss + weighted_dtw

    def training_step(self, batch, batch_idx):
        loss = self._shared_step(batch)
        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True)
        self.log('curriculum_stage', float(self.current_stage), on_epoch=True)
        self.log('mask_lower_bound', self.current_lower_bound, on_epoch=True)
        self.log('mask_upper_bound', self.current_upper_bound, on_epoch=True)
        return loss

    def on_train_epoch_start(self):
        print(f"\n[Stage {self.current_stage}] Epoka {self.current_epoch + 1} | Maskowanie: {self.current_lower_bound * 100:.1f}% - {self.current_upper_bound * 100:.1f}%")

    def validation_step(self, batch, batch_idx):
        loss = self._shared_step(batch)
        self.log('val_loss', loss, on_step=False, on_epoch=True, prog_bar=True)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(self.parameters(), lr=self.base_lr, weight_decay=0.01)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(
            optimizer, T_0=10000, T_mult=1, eta_min=1e-6
        )
        return {
            "optimizer": optimizer,
            "lr_scheduler": {
                "scheduler": scheduler,
                "interval": "step",
                "frequency": 1
            }
        }
    
    def on_save_checkpoint(self, checkpoint):
        checkpoint["curriculum_stage"] = self.current_stage
        checkpoint["curriculum_lb"] = self.current_lower_bound
        checkpoint["curriculum_ub"] = self.current_upper_bound

    def on_load_checkpoint(self, checkpoint):
        # Wymuszenie nowego etapu przy wznawianiu treningu
        if self.rollback_stage is not None:
            stage_bounds = {
                1: (0.10, 0.25), 2: (0.20, 0.35), 3: (0.30, 0.45),
                4: (0.40, 0.55), 5: (0.50, 0.65), 6: (0.60, 0.75),
                7: (0.70, 0.85), 8: (0.80, 0.95), 9: (0.90, 1.00)
            }
            self.current_stage = self.rollback_stage
            bounds = stage_bounds.get(self.rollback_stage, (0.10, 0.25))
            self.current_lower_bound = bounds[0]
            self.current_upper_bound = bounds[1]
            
            print("\n" + "="*70)
            print("[RESUME OVERRIDE] Załadowano wagi modelu, ale NADPISANO stan curriculum!")
            print(f" ➔ Cofałem model do Stage: {self.current_stage}")
            print(f" ➔ Nowy zakres maskowania tokenów: {self.current_lower_bound * 100:.1f}% - {self.current_upper_bound * 100:.1f}%")
            print("="*70)
        else:
            self.current_stage = checkpoint.get("curriculum_stage", 1)
            self.current_lower_bound = checkpoint.get("curriculum_lb", 0.10)
            self.current_upper_bound = checkpoint.get("curriculum_ub", 0.25)
            
            print("\n" + "="*70)
            print("[RESUME - MODEL STATE] Pomyślnie wczytano wagi i stan modelu!")
            print(f" ➔ Aktualny etap nauczania (Stage): {self.current_stage}")
            print(f" ➔ Zakres maskowania tokenów: {self.current_lower_bound * 100:.1f}% - {self.current_upper_bound * 100:.1f}%")
            print("="*70)


# --- CALLBACK DO PROGRAMU NAUCZANIA ---

class AdaptiveCurriculumCallback(Callback):
    def __init__(self, min_delta=1e-4, reset_state_on_load=False):
        super().__init__()
        self.min_delta = min_delta
        self.reset_state_on_load = reset_state_on_load
        self.best_val_loss = float('inf')
        self.patience_counter = 0
        
        self.stages = {
            1: {"bounds": (0.10, 0.25), "patience": 10},
            2: {"bounds": (0.20, 0.35), "patience": 15},
            3: {"bounds": (0.30, 0.45), "patience": 25},
            4: {"bounds": (0.40, 0.55), "patience": 50},
            5: {"bounds": (0.50, 0.65), "patience": 75},
            6: {"bounds": (0.60, 0.75), "patience": 100},
            7: {"bounds": (0.70, 0.85), "patience": 150},
            8: {"bounds": (0.80, 0.95), "patience": 200},
            9: {"bounds": (0.90, 1.00), "patience": 99999}
        }

    def on_validation_epoch_end(self, trainer, pl_module):
        if trainer.sanity_checking:
            return

        metrics = trainer.callback_metrics
        current_val_loss = metrics.get("val_loss")
        
        if current_val_loss is None:
            return

        current_val_loss = current_val_loss.item()
        stage = pl_module.current_stage
        
        if stage >= max(self.stages.keys()):
            return

        required_patience = self.stages[stage]["patience"]

        if current_val_loss < self.best_val_loss - self.min_delta:
            self.best_val_loss = current_val_loss
            self.patience_counter = 0  
        else:
            self.patience_counter += 1  

        if self.patience_counter >= required_patience:
            next_stage = stage + 1
            pl_module.current_stage = next_stage
            pl_module.current_lower_bound = self.stages[next_stage]["bounds"][0]
            pl_module.current_upper_bound = self.stages[next_stage]["bounds"][1]
            
            print(f"\n>>> [CURRICULUM] Strata wypłaszczona na etapie {stage}. Przełączam na STAGE {next_stage}! <<<")
            print(f">>> Nowy zakres maskowania tokenów: {pl_module.current_lower_bound*100:.1f}% - {pl_module.current_upper_bound*100:.1f}% <<<")
            
            for lr_scheduler_config in trainer.lr_scheduler_configs:
                sch = lr_scheduler_config.scheduler
                if isinstance(sch, torch.optim.lr_scheduler.CosineAnnealingWarmRestarts):
                    sch.T_cur = 0  
                    print(">>> [SCHEDULER] Wykonano Cosine Warm Restart! Podbito Learning Rate dla nowego etapu. <<<\n")
            
            for callback in trainer.callbacks:
                if isinstance(callback, EarlyStopping):
                    callback.wait_count = 0
                    callback.best_score = torch.tensor(float('inf'))
            
            gc.collect()                  
            if torch.cuda.is_available():
                torch.cuda.empty_cache()    
                print(">>> [VM CLEANUP] Pamięć RAM i cache VRAM zostały pomyślnie wyczyszczone. <<<")
                    
            self.best_val_loss = float('inf')
            self.patience_counter = 0

    def state_dict(self):
        return {
            "best_val_loss": self.best_val_loss,
            "patience_counter": self.patience_counter,
        }

    def load_state_dict(self, state_dict):
        if self.reset_state_on_load:
            self.best_val_loss = float("inf")
            self.patience_counter = 0
            print("\n[RESUME - CALLBACK STATE] Zresetowano statystyki val_loss. Model uczy się na świeżym zbiorze!")
        else:
            self.best_val_loss = state_dict.get("best_val_loss", float("inf"))
            self.patience_counter = state_dict.get("patience_counter", 0)
            print("\n[RESUME - CALLBACK STATE] Pomyślnie odtworzono stan curriculum z checkpointu.")


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


# --- CUSTOM CALLBACK DO LOGOWANIA GENERACJI ---

class LogGeneratedSamplesCallback(Callback):
    def __init__(self, sample_pairs, tokenizer, every_n_steps=5000, console_chars=1200):
        super().__init__()
        self.samples = sample_pairs
        self.tokenizer = tokenizer
        self.every_n_steps = every_n_steps
        self.console_chars = console_chars
        self._last_logged_step = None

    def _should_log(self, trainer):
        if not self.samples:
            return False
        if self.every_n_steps <= 0:
            return True
        if self._last_logged_step is None:
            return trainer.global_step >= self.every_n_steps
        return trainer.global_step - self._last_logged_step >= self.every_n_steps

    def _clip_for_console(self, text):
        if self.console_chars <= 0 or len(text) <= self.console_chars:
            return text
        return text[: self.console_chars] + "\n... <truncated>"

    def on_validation_epoch_end(self, trainer, pl_module):
        if trainer.sanity_checking:
            return
        if not self._should_log(trainer):
            return
        self._last_logged_step = trainer.global_step

        pl_module.eval()
        epoch = pl_module.current_epoch + 1
        device = pl_module.device
        table_rows = []
        
        comet_logger = None
        for logger in trainer.loggers:
            if isinstance(logger, CometLogger):
                comet_logger = logger.experiment
                break

        lb = pl_module.current_lower_bound
        ub = pl_module.current_upper_bound

        for idx, sample in enumerate(self.samples):
            prompt = sample["instruction"]
            target_code = sample["code"]
            prompt_ids = torch.tensor(self.tokenizer.encode_instruction(prompt), dtype=torch.long).to(device).unsqueeze(0)

            try:
                max_code_len = max(pl_module.model.max_seq_len - prompt_ids.size(1), 1)
                code_ids_raw = self.tokenizer.encode_code(target_code)[:max_code_len]
                x_0 = torch.tensor([code_ids_raw], dtype=torch.long, device=device)
                
                mask_prob = sample_epoch_mask_prob(1, device, lb, ub)
                rand_matrix = torch.rand(1, x_0.size(1), device=device)
                is_masked = (rand_matrix < mask_prob) & (x_0 != self.tokenizer.pad_token_id)
                x_masked = x_0.clone()
                x_masked[is_masked] = self.tokenizer.mask_token_id
                masked_text = self.tokenizer.decode(x_masked[0].tolist(), skip_special_tokens=False)

                with torch.no_grad():
                    logits = pl_module.model(x_masked, prompt_ids, mask_prob.view(-1))
                    pred_ids = logits.argmax(dim=-1)
                    
                    mask_id = self.tokenizer.mask_token_id
                    x_masked_cpu = x_masked[0].cpu().tolist()
                    pred_cpu = pred_ids[0].cpu().tolist()
                    merged = []
                    pred_idx = 0
                    for tok in x_masked_cpu:
                        if tok == mask_id:
                            merged.append(pred_cpu[pred_idx])
                        else:
                            merged.append(tok)
                        pred_idx += 1
                    predicted_text = self.tokenizer.decode(merged, skip_special_tokens=False)
            except Exception as e:
                masked_text = f"<ERROR: {type(e).__name__}: {e}>"
                predicted_text = masked_text

            try:
                with torch.no_grad():
                    gen_ids = pl_module.model.generate(
                        prompt_ids, steps=50, device=device, eos_token_id=self.tokenizer.eos_token_id
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
            comet_logger.log_table("generated_samples", table_rows, step=trainer.global_step)
            
        pl_module.train()


class CometCheckpointUploadCallback(Callback):
    def __init__(self, best_checkpoint_callback, last_checkpoint_callback):
        super().__init__()
        self.best_checkpoint_callback = best_checkpoint_callback
        self.last_checkpoint_callback = last_checkpoint_callback
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
        is_improved = self._uploaded_best_score is None or best_score_value < self._uploaded_best_score
        is_new_path = best_path != self._uploaded_best_path

        if is_improved or is_new_path:
            if self._upload_model(experiment, "LocalConvDiffCoder-best", best_path):
                self._uploaded_best_score = best_score_value
                self._uploaded_best_path = best_path
                print(f">>> [COMET] Zapisano BEST model (val_loss={best_score_value:.6f}) z nadpisaniem. <<<")

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

class DiffCoderTrainer:
    def __init__(self, config):
        self.config = config
        self.tokenizer = CodeTokenizer()
        self.setup_data()
        self.setup_model()

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
        )
        cache_dir = ensure_tokenized_cache(
            csv_path=dataset_path,
            tokenizer=self.tokenizer,
            cache_dir=cache_dir,
            max_prompt_len=self.config.max_prompt_len,
            max_code_len=self.config.max_code_len,
            dataset_fraction=self.config.dataset_fraction,
            chunk_size=self.config.cache_chunk_size,
            encode_batch_size=self.config.encode_batch_size,
            force_rebuild=self.config.rebuild_token_cache,
        )

        full_dataset = TokenizedMemmapDataset(cache_dir)
        train_indices, val_indices = make_train_val_indices(
            len(full_dataset),
            val_split=self.config.val_split,
            max_val_samples=self.config.max_val_samples,
            seed=42,
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

        self.sample_pairs = load_cached_samples(cache_dir)

    def setup_model(self):
        raw_model = LocalConvDiffCoder(
            vocab_size=self.tokenizer.vocab_size,
            mask_token_id=self.tokenizer.mask_token_id,
            pad_token_id=self.tokenizer.pad_token_id,
            hidden_dim=self.config.hidden_dim,
            num_blocks=self.config.num_blocks,
            max_seq_len=self.config.max_prompt_len + self.config.max_code_len,
            dilation_factor=self.config.dilation_factor,
        )
        
        self.lightning_model = DiffCoderLightning(
            model=raw_model,
            base_lr=self.config.base_lr,
            rollback_stage=self.config.rollback_stage, # Przekazanie etapu do nadpisania
            use_ast_loss=self.config.use_ast_loss,
        )

    def train(self):
        best_checkpoint_callback = ModelCheckpoint(
            monitor='val_loss',
            dirpath=self.config.checkpoint_dir,
            filename='diffcoder-{epoch:02d}-{val_loss:.4f}',
            save_top_k=1,
            mode='min'
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
            monitor='val_loss',
            patience=self.config.early_stopping_patience,
            mode='min',
            verbose=True
        )
        
        lr_monitor = LearningRateMonitor(logging_interval='epoch')
        curriculum_callback = AdaptiveCurriculumCallback(
            min_delta=1e-4, 
            reset_state_on_load=self.config.reset_curriculum_state 
        )
        
        sample_logger_callback = LogGeneratedSamplesCallback(
            sample_pairs=self.sample_pairs,
            tokenizer=self.tokenizer,
            every_n_steps=self.config.sample_log_every_n_steps,
            console_chars=self.config.sample_console_chars,
        )
        throughput_logger_callback = ThroughputLoggerCallback(
            every_n_batches=self.config.console_log_every_n_batches
        )

        loggers = []
        comet_logger = None
        datehourstr = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if os.getenv("COMET_API_KEY"):
            comet_logger = CometLogger(
                api_key=os.getenv("COMET_API_KEY"),
                project_name=os.getenv("COMET_PROJECT_NAME"),
                workspace=os.getenv("COMET_WORKSPACE"),
                experiment_name=f"diffcoder-light-train-{datehourstr}"
            )
            loggers.append(comet_logger)

        callbacks = [
            best_checkpoint_callback,
            last_checkpoint_callback,
            early_stop_callback,
            lr_monitor,
            throughput_logger_callback,
            sample_logger_callback,
            curriculum_callback,
        ]

        if self.config.upload_checkpoints_to_comet:
            callbacks.append(
                CometCheckpointUploadCallback(
                    best_checkpoint_callback=best_checkpoint_callback,
                    last_checkpoint_callback=last_checkpoint_callback,
                )
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
            val_check_interval=self.config.val_check_interval,
            limit_val_batches=self.config.limit_val_batches,
            log_every_n_steps=self.config.log_every_n_steps,
            num_sanity_val_steps=self.config.num_sanity_val_steps,
        )

        trainer.fit(
            self.lightning_model, 
            train_dataloaders=self.train_loader, 
            val_dataloaders=self.val_loader,
        )
        
        if self.config.upload_checkpoints_to_comet and comet_logger is not None and best_checkpoint_callback.best_model_path:
            try:
                comet_logger.experiment.log_model(
                    "LocalConvDiffCoder-best",
                    best_checkpoint_callback.best_model_path,
                    overwrite=True,
                )
            except Exception as e:
                print(f"[COMET WARNING] Nie udało się automatycznie zalogować BEST modelu: {e}")

        last_model_path = getattr(last_checkpoint_callback, "last_model_path", "") or last_checkpoint_callback.best_model_path
        if self.config.upload_checkpoints_to_comet and comet_logger is not None and last_model_path:
            try:
                comet_logger.experiment.log_model(
                    "LocalConvDiffCoder-last",
                    last_model_path,
                    overwrite=True,
                )
            except Exception as e:
                print(f"[COMET WARNING] Nie udało się automatycznie zalogować LAST modelu: {e}")

        return best_checkpoint_callback.best_model_path

def env_bool(name, default=False):
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def main():
    torch.backends.cudnn.enabled = True
    load_dotenv()
    
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True
        torch.set_float32_matmul_precision("high")

    class Config:
        max_prompt_len = 96
        max_code_len = 512
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
        sample_log_every_n_steps = int(os.getenv("SAMPLE_LOG_EVERY_N_STEPS", "1000"))
        sample_console_chars = int(os.getenv("SAMPLE_CONSOLE_CHARS", "1200"))
        num_sanity_val_steps = int(os.getenv("NUM_SANITY_VAL_STEPS", "0"))
        early_stopping_patience = 120 
        hidden_dim = 512
        num_blocks = 6
        dilation_factor = int(os.getenv("DILATION_FACTOR", "2"))
        dataset_fraction = float(os.getenv("DATASET_FRACTION", "1.0"))
        cache_chunk_size = int(os.getenv("CACHE_CHUNK_SIZE", "8192"))
        encode_batch_size = int(os.getenv("ENCODE_BATCH_SIZE", "512"))
        rebuild_token_cache = env_bool("REBUILD_TOKEN_CACHE", False)
        use_ast_loss = env_bool("USE_AST_LOSS", False)
        upload_checkpoints_to_comet = env_bool("COMET_UPLOAD_CHECKPOINTS", False)
        base_lr = 5e-5
        
        checkpoint_dir = 'checkpoints'
        
        # Trening startuje od zera, bez resume z checkpointu.
        rollback_stage = int(os.getenv("ROLLBACK_STAGE")) if os.getenv("ROLLBACK_STAGE") else None
        reset_curriculum_state = env_bool("RESET_CURRICULUM_STATE", False)

    config = Config()
    trainer = DiffCoderTrainer(config)
    best_model_path = trainer.train()
    print(f"\nTrening zakończony. Najlepszy checkpoint: {best_model_path}")


if __name__ == "__main__":
    main()
