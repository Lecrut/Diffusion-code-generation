import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class AdaLN(nn.Module):
    """Adaptacyjna normalizacja warstwy (AdaLN)."""
    def __init__(self, channels):
        super().__init__()
        self.norm = nn.LayerNorm(channels, elementwise_affine=False)
        self.linear = nn.Linear(channels, channels * 2)

    def forward(self, x, t_emb):
        # t_emb generuje parametry skali (gamma) i przesunięcia (beta)
        gate = self.linear(t_emb).unsqueeze(1)
        gamma, beta = gate.chunk(2, dim=-1)
        return self.norm(x) * (1 + gamma) + beta

class CNNBlock(nn.Module):
    """Pojedynczy blok splotowy z obsługą dylacji (dilation).
    Dylacja pozwala zwiększyć efektywne okno recepcyjne bez zwiększania
    liczby parametrów ani głębokości sieci.
    """
    def __init__(self, dim, kernel_size=5, dilation=1):
        super().__init__()
        # padding tak dobrany, by zachować tę samą długość wyjścia jak wejścia
        padding = ((kernel_size - 1) // 2) * dilation
        self.conv = nn.Conv1d(dim, dim, kernel_size, padding=padding, dilation=dilation)
        self.ln = AdaLN(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, dim * 2),
            nn.GELU(),
            nn.Linear(dim * 2, dim)
        )

    def forward(self, x, t_emb):
        res = x
        x = x.transpose(1, 2)
        x = self.conv(x).transpose(1, 2)
        x = self.ln(x, t_emb)
        x = x + res
        
        # Refinement (MLP)
        x = x + self.mlp(self.ln(x, t_emb))
        return x

class LocalConvDiffCoder(nn.Module):
    def __init__(
        self,
        vocab_size,
        mask_token_id,
        pad_token_id,
        hidden_dim=256,
        num_blocks=4,
        max_seq_len=1024,
        dilation_factor=2,
    ):
        super().__init__()
        self.vocab_size = vocab_size
        self.mask_token_id = mask_token_id
        self.pad_token_id = pad_token_id
        self.max_seq_len = max_seq_len
        
        self.token_embedding = nn.Embedding(vocab_size, hidden_dim)
        self.pos_emb = nn.Parameter(torch.zeros(1, max_seq_len, hidden_dim))
                
        self.time_mlp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        self.blocks = nn.ModuleList([
            CNNBlock(
                hidden_dim,
                kernel_size=5 + (i * 2),
                dilation=(dilation_factor ** i)
            ) for i in range(num_blocks)
        ])
        
        self.ln_final = nn.LayerNorm(hidden_dim)
        self.lm_head = nn.Linear(hidden_dim, vocab_size)

    def _get_timestep_embedding(self, timesteps, dim):
        half_dim = dim // 2
        exponent = -math.log(10000) * torch.arange(half_dim, device=timesteps.device) / (half_dim - 1)
        emb = torch.exp(exponent)
        emb = timesteps[:, None] * emb[None, :]
        return torch.cat([emb.sin(), emb.cos()], dim=-1)


    def forward(self, x, prompt_ids, t):
        code_len = x.size(1)
        prompt_len = prompt_ids.size(1)
        if prompt_len + code_len > self.max_seq_len:
            available_prompt_len = self.max_seq_len - code_len
            if available_prompt_len <= 0:
                prompt_ids = prompt_ids[:, :0]
            else:
                prompt_ids = prompt_ids[:, :available_prompt_len]
            prompt_len = prompt_ids.size(1)

        # 2. Embeddingi promptu i kodu + pozycje
        if prompt_len > 0:
            prompt_emb = self.token_embedding(prompt_ids)
            code_emb = self.token_embedding(x)
            x_emb = torch.cat([prompt_emb, code_emb], dim=1)
        else:
            x_emb = self.token_embedding(x)
        x_emb = x_emb + self.pos_emb[:, :x_emb.size(1), :]


        # zerowanie paddingow by nie wpływały na wynik splotu
        if prompt_len > 0:
            prompt_mask = (prompt_ids != self.pad_token_id).float().unsqueeze(-1)
            code_mask = (x != self.pad_token_id).float().unsqueeze(-1)
            seq_mask = torch.cat([prompt_mask, code_mask], dim=1)
        else:
            seq_mask = (x != self.pad_token_id).float().unsqueeze(-1)
        x_emb = x_emb * seq_mask
        
        
        # 3. Czas t
        t_emb = self.time_mlp(self._get_timestep_embedding(t, x_emb.size(-1)))
        
        # 4. Przetwarzanie CNN
        features = []
        for block in self.blocks:
            x_emb = block(x_emb, t_emb)
            features.append(x_emb)
            
        x_out = torch.stack(features).mean(dim=0)
        logits = self.lm_head(self.ln_final(x_out))
        return logits[:, prompt_len:, :]

    @torch.no_grad()
    def generate(self, prompt_ids, steps=50, device="cuda", eos_token_id=None):
        if prompt_ids.dim() == 1:
            prompt_ids = prompt_ids.unsqueeze(0)
        prompt_ids = prompt_ids.to(device)
        prompt_len = prompt_ids.size(1)
        code_len = max(self.max_seq_len - prompt_len, 1)
            
        seq = torch.full((1, code_len), self.mask_token_id, dtype=torch.long, device=device)
        
        for step in range(steps):
            t = torch.full((1,), (steps - step) / steps, device=device)
            
            logits = self.forward(seq, prompt_ids, t)
            
            probs = F.softmax(logits, dim=-1)
            conf, pred = probs.max(dim=-1)
            
            ratio = 1.0 - (step + 1) / steps
            num_to_mask = int(code_len * ratio)
            
            if num_to_mask > 0:
                _, mask_idx = torch.topk(conf, k=num_to_mask, largest=False)
                pred[0, mask_idx[0]] = self.mask_token_id
            
            seq = pred
            
        if eos_token_id is not None:
            eos_pos = (seq[0] == eos_token_id).nonzero(as_tuple=False)
            if eos_pos.numel() > 0:
                cut = int(eos_pos[0].item()) + 1
                seq = seq[:, :cut]

        return seq