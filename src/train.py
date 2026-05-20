from functools import partial
from pathlib import Path
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from tqdm import tqdm

from diffusion.model import LocalConvDiffCoder
from tokenizer import CodeTokenizer 


class CodeInstructionDataset(Dataset):
    def __init__(self, csv_file, tokenizer, max_prompt_len=128, max_code_len=1024):
        self.df = pd.read_csv(csv_file)
        self.df = self.df[['instruction', 'code']].dropna()
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
        
        prompt_ids_raw = self.tokenizer.encode(row['instruction'])
        code_ids_raw = self.tokenizer.encode(row['code'])
        
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


def train_diffcoder(model, dataloader, optimizer, epochs, device):
    model.train() 
    use_amp = device == "cuda"
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp)
    
    for epoch in range(epochs):
        total_loss = 0
        progress_bar = tqdm(enumerate(dataloader), total=len(dataloader), desc=f"Epoka {epoch+1}/{epochs}")
        
        for batch_idx, batch in progress_bar:
            x_0 = batch['code_ids'].to(device)
            prompt_ids = batch['prompt_ids'].to(device)
            
            batch_size, seq_len = x_0.shape
            
            t = torch.rand(batch_size, device=device)
            
            mask_prob = t.view(batch_size, 1)
            rand_matrix = torch.rand(batch_size, seq_len, device=device)
            
            is_masked = (rand_matrix < mask_prob) & (x_0 != model.pad_token_id)
            
            x_t = x_0.clone()
            x_t[is_masked] = model.mask_token_id
            
            optimizer.zero_grad()
            with torch.amp.autocast("cuda", enabled=use_amp):
                logits = model(x_t, prompt_ids, t)
                
                masked_logits = logits[is_masked] 
                masked_targets = x_0[is_masked]
                
                if masked_targets.numel() > 0:
                    loss = F.cross_entropy(masked_logits, masked_targets)
                else:
                    loss = torch.tensor(0.0, device=device, requires_grad=True)
            
            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            
            total_loss += loss.item()
            progress_bar.set_postfix({'loss': f"{loss.item():.4f}"})
            
        avg_loss = total_loss / len(dataloader)
        print(f"\n--- Zakończono Epokę {epoch+1} | Średni błąd: {avg_loss:.4f} ---")
        
        checkpoint = {
            "epoch": epoch + 1,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
        }
        torch.save(checkpoint, f"diffcoder_epoch_{epoch+1}.pt")
        print("Checkpoint zapisany!\n")


if __name__ == "__main__":
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Rozpoczynam trening na: {DEVICE}")

    if DEVICE == "cuda":
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True
        torch.set_float32_matmul_precision("high")
    
    tokenizer = CodeTokenizer()
    
    MAX_PROMPT_LEN = 96
    MAX_CODE_LEN = 1024
    BATCH_SIZE = 32
    NUM_WORKERS = 5
    EPOCHS = 20
    
    model = LocalConvDiffCoder(
        vocab_size=tokenizer.vocab_size,
        mask_token_id=tokenizer.mask_token_id,
        pad_token_id=tokenizer.pad_token_id,
        hidden_dim=256,
        num_blocks=4,
        max_seq_len=MAX_PROMPT_LEN + MAX_CODE_LEN
    ).to(DEVICE)
    
    repo_root = Path(__file__).resolve().parents[1]
    dataset_path = repo_root / "data" / "dataset.csv"
    dataset = CodeInstructionDataset(
        str(dataset_path),
        tokenizer,
        max_prompt_len=MAX_PROMPT_LEN,
        max_code_len=MAX_CODE_LEN,
    )
    collate_fn = partial(
        collate_batch,
        pad_id=tokenizer.pad_token_id,
        max_prompt_len=MAX_PROMPT_LEN,
        max_code_len=MAX_CODE_LEN,
    )
    dataloader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=DEVICE == "cuda",
        persistent_workers=NUM_WORKERS > 0,
        collate_fn=collate_fn,
    )
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.01)
    
    train_diffcoder(model, dataloader, optimizer, EPOCHS, DEVICE)