import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class AdaLN(nn.Module):
    """Adaptacyjna normalizacja warstwy (AdaLN) inspirowana artykułem[cite: 519, 521]."""
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
    """Pojedynczy blok splotowy"""
    def __init__(self, dim, kernel_size=5):
        super().__init__()
        # Splot 1D zapewnia lokalne okno kontekstowe
        self.conv = nn.Conv1d(dim, dim, kernel_size, padding=kernel_size // 2)
        self.ln = AdaLN(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, dim * 2),
            nn.GELU(),
            nn.Linear(dim * 2, dim)
        )

    def forward(self, x, t_emb):
        # Przejście przez CNN (wymaga zamiany wymiarów dla Conv1d)
        res = x
        x = x.transpose(1, 2)
        x = self.conv(x).transpose(1, 2)
        x = self.ln(x, t_emb)
        x = x + res
        
        # Refinement (MLP)
        x = x + self.mlp(self.ln(x, t_emb))
        return x

class LocalConvDiffCoder(nn.Module):
    def __init__(self, vocab_size, mask_token_id, hidden_dim=512, num_blocks=6, max_seq_len=1024):
        super().__init__()
        self.vocab_size = vocab_size
        self.mask_token_id = mask_token_id
        self.max_seq_len = max_seq_len
        
        self.token_embedding = nn.Embedding(vocab_size, hidden_dim)
        self.pos_emb = nn.Parameter(torch.zeros(1, max_seq_len, hidden_dim))
        
        # MLP przetwarzający krok czasowy t
        self.time_mlp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Stos nakładających się bloków CNN
        self.blocks = nn.ModuleList([
            CNNBlock(hidden_dim, kernel_size=5 + (i * 2)) for i in range(num_blocks)
        ])
        
        self.ln_final = nn.LayerNorm(hidden_dim)
        self.lm_head = nn.Linear(hidden_dim, vocab_size)

    def _get_timestep_embedding(self, timesteps, dim):
        half_dim = dim // 2
        exponent = -math.log(10000) * torch.arange(half_dim, device=timesteps.device) / (half_dim - 1)
        emb = torch.exp(exponent)
        emb = timesteps[:, None] * emb[None, :]
        return torch.cat([emb.sin(), emb.cos()], dim=-1)

    def forward(self, x, t):
        # 1. Embeddings i czas
        t_emb = self.time_mlp(self._get_timestep_embedding(t, x.size(-1) if hasattr(x, 'size') else 512))
        x = self.token_embedding(x) + self.pos_emb[:, :x.size(1), :]
        
        # 2. Przetwarzanie przez Overlapping CNN Blocks
        features = []
        for block in self.blocks:
            x = block(x, t_emb)
            features.append(x)
        
        # 3. Aggregation Layer (ze schematu - proste uśrednienie cech z różnych poziomów)
        x = torch.stack(features).mean(dim=0)
        
        # 4. Classification Head
        return self.lm_head(self.ln_final(x))

    @torch.no_grad()
    def generate(self, steps=50, device="cuda"):
        # Start: 100% masked sequence [cite: 78, 84]
        seq = torch.full((1, self.max_seq_len), self.mask_token_id, dtype=torch.long, device=device)
        
        for step in range(steps):
            t = torch.full((1,), (steps - step) / steps, device=device)
            logits = self.forward(seq, t)
            
            # Próbkowanie (Porcjowanie)
            probs = F.softmax(logits, dim=-1)
            conf, pred = probs.max(dim=-1)
            
            # Strategia odmaskowywania: zostawiamy tylko najbardziej pewne tokeny 
            ratio = 1.0 - (step + 1) / steps
            num_to_mask = int(self.max_seq_len * ratio)
            
            if num_to_mask > 0:
                _, mask_idx = torch.topk(conf, k=num_to_mask, largest=False)
                pred[0, mask_idx[0]] = self.mask_token_id
            
            seq = pred
            
        return seq