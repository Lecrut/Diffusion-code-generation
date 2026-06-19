from functools import partial
from pathlib import Path
import os
import random
import ast as _ast
import torch
import torch.nn as nn
import gc 
import pandas as pd
from torch.utils.data import Dataset, DataLoader, random_split
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor, EarlyStopping, Callback
from pytorch_lightning.loggers import CometLogger
from dotenv import load_dotenv
from datetime import timedelta

# Importy z Twoich modułów
from diffusion.model import LocalConvDiffCoder
from tokenizer import CodeTokenizer 
from diffusion.loss import CalculateLoss


def sample_epoch_mask_prob(batch_size, device, lower_bound, upper_bound):
    return lower_bound + torch.rand(batch_size, device=device) * (upper_bound - lower_bound)


# --- DATASET & COLLATE (AST BIGRAMY) ---

class CodeInstructionDataset(Dataset):
    def __init__(self, csv_file, tokenizer, max_prompt_len=128, max_code_len=1024, dataset_fraction=1.0, seed=42):
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
        
        self.node_vocab = {}
        for code in self.df['code'].astype(str):
            try:
                tree = _ast.parse(code)
                for parent in _ast.walk(tree):
                    p_name = type(parent).__name__
                    for child in _ast.iter_child_nodes(parent):
                        c_name = type(child).__name__
                        bigram = f"{p_name}->{c_name}"
                        if bigram not in self.node_vocab:
                            self.node_vocab[bigram] = len(self.node_vocab)
            except Exception:
                continue
        self.ast_dim = len(self.node_vocab)

    def __len__(self):
        return len(self.df)

    def _pad_or_truncate(self, ids, max_len):
        return ids[:max_len] if len(ids) > max_len else ids

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        prompt_ids = self._pad_or_truncate(self.tokenizer.encode_instruction(row['instruction']), self.max_prompt_len)
        code_ids = self._pad_or_truncate(self.tokenizer.encode_code(row['code']), self.max_code_len)
        
        try:
            tree = _ast.parse(row['code'])
            counts = [0] * self.ast_dim
            for parent in _ast.walk(tree):
                p_name = type(parent).__name__
                for child in _ast.iter_child_nodes(parent):
                    c_name = type(child).__name__
                    bigram = f"{p_name}->{c_name}"
                    idx_t = self.node_vocab.get(bigram)
                    if idx_t is not None:
                        counts[idx_t] += 1
            ast_vec = torch.tensor(counts, dtype=torch.float)
        except Exception:
            ast_vec = torch.zeros(self.ast_dim, dtype=torch.float)

        return {'prompt_ids': prompt_ids, 'code_ids': code_ids, 'ast_vec': ast_vec}


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
        if prompt_pad > 0: prompt_ids = prompt_ids + [pad_id] * prompt_pad
        if code_pad > 0: code_ids = code_ids + [pad_id] * code_pad
        prompt_tensors.append(torch.tensor(prompt_ids, dtype=torch.long))
        code_tensors.append(torch.tensor(code_ids, dtype=torch.long))

    result = {'prompt_ids': torch.stack(prompt_tensors, dim=0), 'code_ids': torch.stack(code_tensors, dim=0)}
    if 'ast_vec' in batch[0]:
        result['ast_vec'] = torch.stack([item['ast_vec'] for item in batch], dim=0)
    return result


# --- LIGHTNING MODULE ---

class DiffCoderLightning(pl.LightningModule):
    def __init__(self, model, base_lr=5e-5, rollback_stage=None):
        super().__init__()
        self.model = model
        self.base_lr = base_lr
        self.rollback_stage = None
        
        self.current_stage = 1
        self.current_lower_bound = 0.10
        self.current_upper_bound = 0.25
        
        self.loss_fn = CalculateLoss(
            gamma=1.0,
            ce_weight=1.0,
            dtw_weight=1.0,
            embedding_matrix=getattr(model, 'embedding', None).weight if hasattr(model, 'embedding') else None,
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
        
        logits = self.model(x_t, prompt_ids, t)
        masked_logits = logits[is_masked]
        masked_targets = x_0[is_masked]

        if masked_targets.numel() == 0:
            return torch.tensor(0.0, device=self.device, requires_grad=True)

        ast_embeddings = self._get_ast_embeddings(batch)
        
        _, ce_loss, dtw_loss = self.loss_fn(
            full_logits=logits, 
            masked_logits=masked_logits, 
            masked_targets=masked_targets,
            ast_embeddings=ast_embeddings,
        )
        
        mean_t = t.mean()
        weighted_dtw = (0.1 + 0.4 * mean_t) * dtw_loss
        loss = ce_loss + weighted_dtw
        
        return loss

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
                "interval": "epoch",
                "frequency": 1
            }
        }
    
    def on_save_checkpoint(self, checkpoint):
        checkpoint["curriculum_stage"] = self.current_stage
        checkpoint["curriculum_lb"] = self.current_lower_bound
        checkpoint["curriculum_ub"] = self.current_upper_bound

    def on_load_checkpoint(self, checkpoint):
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


# --- CUSTOM CALLBACK DO LOGOWANIA GENERACJI ---

class LogGeneratedSamplesCallback(Callback):
    def __init__(self, sample_pairs, tokenizer):
        super().__init__()
        self.samples = sample_pairs
        self.tokenizer = tokenizer

    def on_validation_epoch_end(self, trainer, pl_module):
        if trainer.sanity_checking:
            return

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
                code_ids_raw = self.tokenizer.encode_code(target_code)
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

            if comet_logger is not None:
                comet_logger.log_text(
                    f"Epoch {epoch} | sample {idx}\nPROMPT:\n{prompt}\n\nGROUND_TRUTH:\n{target_code}"
                    f"\n\nMASKED_GROUND_TRUTH:\n{masked_text}\n\nPREDICTED_THIS_ITERATION:\n{predicted_text}"
                    f"\n\nGENERATED:\n{gen_text}",
                    step=epoch,
                )
                table_rows.append({
                    "epoch": epoch, "sample": idx, "prompt": prompt, "ground_truth": target_code,
                    "masked_ground_truth": masked_text, "predicted_this_iteration": predicted_text, "generated": gen_text
                })
            else:
                print("-" * 80)
                print(f"Epoch {epoch} | sample {idx}\nMASKED_GROUND_TRUTH:\n{masked_text}\nGENERATED:\n{gen_text}")

        if comet_logger is not None and table_rows:
            comet_logger.log_table("generated_samples", table_rows, step=epoch)
            
        pl_module.train()


# --- GŁÓWNY PROCES TRENINGOWY ---

class DiffCoderTrainer:
    def __init__(self, config):
        self.config = config
        self.tokenizer = CodeTokenizer()
        self.setup_data()
        self.setup_model()

    def setup_data(self):
        repo_root = Path(__file__).resolve().parents[1] if '__file__' in locals() else Path(".")
        dataset_path = repo_root / "data" / "dataset.csv"
        
        dataset = CodeInstructionDataset(
            str(dataset_path), self.tokenizer,
            max_prompt_len=self.config.max_prompt_len,
            max_code_len=self.config.max_code_len,
            dataset_fraction=self.config.dataset_fraction
        )

        val_size = max(1, int(len(dataset) * self.config.val_split))
        train_size = len(dataset) - val_size
        self.train_dataset, self.val_dataset = random_split(
            dataset, [train_size, val_size], generator=torch.Generator().manual_seed(42)
        )

        collate_fn = partial(
            collate_batch, pad_id=self.tokenizer.pad_token_id,
            max_prompt_len=self.config.max_prompt_len, max_code_len=self.config.max_code_len
        )
        
        self.train_loader = DataLoader(
            self.train_dataset, batch_size=self.config.batch_size, shuffle=True,
            num_workers=self.config.num_workers, pin_memory=True, collate_fn=collate_fn
        )
        self.val_loader = DataLoader(
            self.val_dataset, batch_size=self.config.batch_size, shuffle=False,
            num_workers=self.config.num_workers, pin_memory=True, collate_fn=collate_fn
        )

        self.sample_pairs = []
        rng = random.Random(42)
        sample_indices = rng.sample(range(len(dataset)), min(3, len(dataset)))
        for idx in sample_indices:
            row = dataset.df.iloc[idx]
            self.sample_pairs.append({"instruction": str(row["instruction"]), "code": str(row["code"])})

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
            save_top_k=1,
            every_n_epochs=1,
            save_on_train_epoch_end=True 
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
            tokenizer=self.tokenizer
        )

        loggers = []
        comet_logger = None
        if os.getenv("COMET_API_KEY"):
            comet_logger = CometLogger(
                api_key=os.getenv("COMET_API_KEY"),
                project_name=os.getenv("COMET_PROJECT_NAME"),
                workspace=os.getenv("COMET_WORKSPACE")
            )
            loggers.append(comet_logger)

        trainer = pl.Trainer(
            max_epochs=self.config.epochs,
            accelerator='gpu' if torch.cuda.is_available() else 'cpu',
            devices=1 if torch.cuda.is_available() else "auto",
            accumulate_grad_batches=self.config.accumulation_steps,
            callbacks=[best_checkpoint_callback, last_checkpoint_callback, early_stop_callback, lr_monitor, sample_logger_callback, curriculum_callback],
            logger=loggers if loggers else True,
            precision="16-mixed" if torch.cuda.is_available() else 32,
            gradient_clip_val=1.0
        )

        ckpt_to_resume = None
        if self.config.resume_from_checkpoint and self.config.resume_ckpt_name:
            target_ckpt = Path(self.config.checkpoint_dir) / self.config.resume_ckpt_name
            if target_ckpt.exists():
                ckpt_to_resume = str(target_ckpt)
                print(f"\n>>> [RESUME] Odszukano wyznaczony plik: {ckpt_to_resume} <<<\n")
            else:
                print(f"\n>>> [WARNING] Nie znaleziono pliku '{self.config.resume_ckpt_name}' w katalogu {self.config.checkpoint_dir}! Rozpoczynam od zera. <<<\n")

        trainer.fit(
            self.lightning_model, 
            train_dataloaders=self.train_loader, 
            val_dataloaders=self.val_loader,
            ckpt_path=ckpt_to_resume 
        )
        
        if comet_logger is not None and best_checkpoint_callback.best_model_path:
            try:
                print(">>> [COMET] Rejestruję najlepszy model w chmurze Comet ML... <<<")
                comet_logger.experiment.log_model("LocalConvDiffCoder", best_checkpoint_callback.best_model_path)
            except Exception as e:
                print(f"[COMET WARNING] Nie udało się automatycznie zalogować modelu: {e}")

        return best_checkpoint_callback.best_model_path


def main():
    torch.backends.cudnn.enabled = False
    load_dotenv()
    
    if torch.cuda.is_available():
        # torch.backends.cuda.matmul.allow_tf32 = True
        # torch.backends.cudnn.allow_tf32 = True
        torch.set_float32_matmul_precision("high")

    class Config:
        max_prompt_len = 96
        max_code_len = 512
        batch_size = 4
        accumulation_steps = 8
        num_workers = 3
        epochs = 1500 
        val_split = 0.05
        early_stopping_patience = 120 
        hidden_dim = 512
        num_blocks = 6
        dilation_factor = int(os.getenv("DILATION_FACTOR", "2"))
        dataset_fraction = float(os.getenv("DATASET_FRACTION", "1.0"))
        base_lr = 5e-5
        
        checkpoint_dir = 'checkpoints'
        
        # --- ZARZĄDZANIE WZNAWIANIEM TRENINGU ---
        resume_from_checkpoint = True
        resume_ckpt_name = "last-v1.ckpt" # Bezpośrednie celowanie w wirtualkę
        reset_curriculum_state = True # Reset liczników val_loss dla nowej paczki 15k danych

    config = Config()
    trainer = DiffCoderTrainer(config)
    best_model_path = trainer.train()
    print(f"\nTrening zakończony. Najlepszy checkpoint: {best_model_path}")


if __name__ == "__main__":
    main()