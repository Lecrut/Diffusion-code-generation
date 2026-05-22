import math

import torch
import torch.nn as nn
import torch.nn.functional as F




def cosine_beta_schedule(T: int, s: float = 0.008):
    """
    Cosinusowy harmonogram szumu (Nichol & Dhariwal, 2021).
    Zwraca:
      betas       – (T,) współczynniki szumu β_t
      alphas_bar  – (T,) skumulowane iloczyny ā_t dla t = 1..T
    """
    steps = torch.arange(T + 1, dtype=torch.float64)
    f = torch.cos(((steps / T) + s) / (1.0 + s) * math.pi / 2.0) ** 2
    alphas_bar = f / f[0]                                  # ā_0 = 1
    betas = 1.0 - (alphas_bar[1:] / alphas_bar[:-1])
    betas = torch.clamp(betas, min=1e-5, max=0.999).float()
    alphas_bar = alphas_bar[1:].float()                    # ā_1 … ā_T
    return betas, alphas_bar



class FiLM(nn.Module):
    """
    Wstrzykuje wektor warunkujący (czas t + prompt) jako parę (γ, β):
        FiLM(x) = x * (1 + γ) + β
    Parametry są generowane przez projekcję liniową z cond_dim.
    """
    def __init__(self, num_features: int, cond_dim: int):
        super().__init__()
        self.proj = nn.Linear(cond_dim, num_features * 2)

    def forward(self, x: torch.Tensor, cond: torch.Tensor) -> torch.Tensor:
        # x: (B, L, C)   cond: (B, cond_dim)
        gamma, beta = self.proj(cond).chunk(2, dim=-1)     # (B, C) każdy
        return x * (1.0 + gamma.unsqueeze(1)) + beta.unsqueeze(1)




class GatedConv1d(nn.Module):
    """
    Konwolucja bramkowana: out = tanh(W_f * x) ⊙ σ(W_g * x).
    Podwójna liczba kanałów wyjściowych jest obsługiwana wewnętrznie.
    """
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int,
        stride: int = 1,
        padding: int = 0,
        dilation: int = 1,
    ):
        super().__init__()
        self.conv = nn.Conv1d(
            in_channels, out_channels * 2, kernel_size,
            stride=stride, padding=padding, dilation=dilation,
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h_val, h_gate = self.conv(x).chunk(2, dim=1)
        return torch.tanh(h_val) * torch.sigmoid(h_gate)



class DownBlock(nn.Module):
    """
    Ścieżka w dół (encoder FPN).
    Gated Conv1D ze stride=2 zmniejsza długość sekwencji 2×,
    FiLM wstrzykuje warunkowanie po normalizacji.
    """
    def __init__(self, in_dim: int, out_dim: int, cond_dim: int):
        super().__init__()
        # kernel=4, stride=2, padding=1  ⟹  L → L // 2 (dokładnie)
        self.conv = GatedConv1d(in_dim, out_dim, kernel_size=4, stride=2, padding=1)
        self.norm = nn.LayerNorm(out_dim)
        self.film = FiLM(out_dim, cond_dim)

    def forward(self, x: torch.Tensor, cond: torch.Tensor) -> torch.Tensor:
        # x: (B, L, C) → operacje splotowe wymagają (B, C, L)
        h = self.conv(x.transpose(1, 2)).transpose(1, 2)  # (B, L//2, out_dim)
        return self.film(self.norm(h), cond)


class DilatedGatedBlock(nn.Module):
    """
    Wąskie gardło (bottleneck): WaveNet-style dilated Gated Conv1D.
    Wykładniczo rosnące dylatacje (1, 2, 4, 8, …) budują globalne pole
    recepcyjne bez poolingu. Połączenie residualne chroni gradient.
    """
    def __init__(
        self, dim: int, cond_dim: int, kernel_size: int = 3, dilation: int = 1
    ):
        super().__init__()
        padding = (kernel_size - 1) * dilation // 2
        self.conv = GatedConv1d(dim, dim, kernel_size, padding=padding, dilation=dilation)
        self.norm = nn.LayerNorm(dim)
        self.film = FiLM(dim, cond_dim)

    def forward(self, x: torch.Tensor, cond: torch.Tensor) -> torch.Tensor:
        h = self.conv(x.transpose(1, 2)).transpose(1, 2)
        h = self.film(self.norm(h), cond)
        return x + h                                       # połączenie residualne


class UpBlock(nn.Module):
    """
    Ścieżka w górę (decoder FPN).
    ConvTranspose1d ze stride=2 zwiększa długość 2×, następnie Skip Connection
    łączy cechy z odpowiadającego DownBlock, a FiLM moduluje wynik.
    """
    def __init__(self, in_dim: int, out_dim: int, cond_dim: int):
        super().__init__()
        self.up = nn.ConvTranspose1d(in_dim, out_dim, kernel_size=4, stride=2, padding=1)
        self.out_gate = nn.Linear(out_dim, out_dim)
        self.skip_proj = nn.Linear(out_dim * 2, out_dim)
        self.norm = nn.LayerNorm(out_dim)
        self.film = FiLM(out_dim, cond_dim)

    def forward(
        self, x: torch.Tensor, skip: torch.Tensor, cond: torch.Tensor
    ) -> torch.Tensor:
        h = self.up(x.transpose(1, 2)).transpose(1, 2)    # (B, L*2, out_dim)

        min_len = min(h.size(1), skip.size(1))
        h = h[:, :min_len, :]
        skip = skip[:, :min_len, :]

        h = torch.sigmoid(self.out_gate(h)) * h

        h = self.skip_proj(torch.cat([h, skip], dim=-1))

        return self.film(self.norm(h), cond)



class ContinuousDiffusionUNet(nn.Module):
    """
    Model ciągłej dyfuzji (Continuous DDPM) operujący bezpośrednio
    w przestrzeni osadzeń tokenów (bez maskowania, bez lm_head).

    Cztery fazy działania:
      1. Warunkowanie  – embeddingiy promptu (mean-pool) + sinusoidalny czas t
                         → wspólny wektor cond (używany przez FiLM w każdym bloku)
      2. Szumienie     – q(z_t | z_0) = √ā_t · z_0 + √(1-ā_t) · ε
      3. Odszumianie   – 1D U-Net z Gated Conv1D + FiLM przewiduje z_0 z z_t
      4. Rounding      – z_0 → cosine similarity z macierzą Embedding → argmax → tokeny

    Parametry:
      vocab_size    – rozmiar słownika tokenizera
      pad_token_id  – id tokenu padding
      hidden_dim    – wymiar bazowy osadzeń (kanały wejściowe U-Netu)
      num_down      – liczba kroków down-sample (i symetrycznych up-sample)
      num_bottleneck– liczba bloków dilated w wąskim gardle
      max_seq_len   – maksymalna łączna długość (prompt + kod)
      T             – liczba kroków dyfuzji
    """

    def __init__(
        self,
        vocab_size: int,
        pad_token_id: int,
        hidden_dim: int = 256,
        num_down: int = 2,
        num_bottleneck: int = 4,
        max_seq_len: int = 1024,
        T: int = 1000,
    ):
        super().__init__()
        self.vocab_size  = vocab_size
        self.pad_token_id = pad_token_id
        self.hidden_dim  = hidden_dim
        self.max_seq_len = max_seq_len
        self.T           = T

        betas, alphas_bar = cosine_beta_schedule(T)
        self.register_buffer("betas",                     betas)
        self.register_buffer("alphas_bar",                alphas_bar)
        self.register_buffer("sqrt_alphas_bar",           alphas_bar.sqrt())
        self.register_buffer("sqrt_one_minus_alphas_bar", (1.0 - alphas_bar).sqrt())


        self.token_embedding = nn.Embedding(vocab_size, hidden_dim)
        self.pos_emb = nn.Parameter(torch.zeros(1, max_seq_len, hidden_dim))

        self.time_mlp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * 4),
            nn.SiLU(),
            nn.Linear(hidden_dim * 4, hidden_dim),
        )

        # cond_dim = hidden_dim (wspólny wymiar dla FiLM we wszystkich blokach)
        self.cond_proj = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        cond_dim = hidden_dim

        # dims[0] = hidden_dim, dims[1] = 2*hidden_dim, …
        dims = [hidden_dim * (2 ** i) for i in range(num_down + 1)]

        self.down_blocks = nn.ModuleList([
            DownBlock(dims[i], dims[i + 1], cond_dim)
            for i in range(num_down)
        ])

        self.bottleneck = nn.ModuleList([
            DilatedGatedBlock(dims[-1], cond_dim, dilation=2 ** i)
            for i in range(num_bottleneck)
        ])

        self.up_blocks = nn.ModuleList([
            UpBlock(dims[num_down - i], dims[num_down - i - 1], cond_dim)
            for i in range(num_down)
        ])

        self.out_norm = nn.LayerNorm(hidden_dim)

    def _timestep_emb(self, t: torch.Tensor) -> torch.Tensor:
        """Sinusoidalne osadzenie kroku t (obsługuje float i int)."""
        half = self.hidden_dim // 2
        freqs = torch.exp(
            -math.log(10000.0)
            * torch.arange(half, dtype=torch.float32, device=t.device)
            / max(half - 1, 1)
        )
        emb = t.float()[:, None] * freqs[None, :]         # (B, half)
        return torch.cat([emb.sin(), emb.cos()], dim=-1)  # (B, hidden_dim)

    def _build_cond(
        self, t: torch.Tensor, prompt_ids: torch.Tensor
    ) -> torch.Tensor:
        """
        Buduje wektor warunkujący: FiLM(t) + FiLM(prompt).
        Prompt jest mean-poolowany z maskowaniem paddingu.
        """
        t_emb = self.time_mlp(self._timestep_emb(t))      # (B, D)

        p_emb = self.token_embedding(prompt_ids)           # (B, P, D)
        pmask = (prompt_ids != self.pad_token_id).float().unsqueeze(-1)  # (B, P, 1)
        p_len = pmask.sum(dim=1).clamp(min=1.0)            # (B, 1)
        p_mean = (p_emb * pmask).sum(dim=1) / p_len       # (B, D)

        return self.cond_proj(torch.cat([t_emb, p_mean], dim=-1))  # (B, D)


    def forward(
        self,
        z_noisy: torch.Tensor,    # (B, L, D)  ciągłe, zaszumione osadzenia kodu
        prompt_ids: torch.Tensor,  # (B, P)     dyskretne tokeny promptu
        t: torch.Tensor,           # (B,)       int 1..T
    ) -> torch.Tensor:             # → (B, L, D)  przewidziane czyste Z_0
        B, L, D = z_noisy.shape

        cond = self._build_cond(t, prompt_ids)             # (B, D)


        with torch.no_grad():
            p_emb = self.token_embedding(prompt_ids)       # (B, P, D)
        P = p_emb.size(1)

        seq = torch.cat([p_emb, z_noisy], dim=1)          # (B, P+L, D)
        seq = seq + self.pos_emb[:, : seq.size(1), :]

        pmask = (prompt_ids != self.pad_token_id).float().unsqueeze(-1)
        code_mask = torch.ones(B, L, 1, device=seq.device)
        seq_mask = torch.cat([pmask, code_mask], dim=1)
        seq = seq * seq_mask

        # ── Ścieżka w dół ───────────────────────────────────────────────────
        skips: list[torch.Tensor] = []
        h = seq
        for down in self.down_blocks:
            skips.append(h)                                # zapisujemy PRZED down-sample
            h = down(h, cond)

        # ── Wąskie gardło (dilated) ──────────────────────────────────────────
        for btn in self.bottleneck:
            h = btn(h, cond)

        # ── Ścieżka w górę (ze skip connections) ────────────────────────────
        for up, skip in zip(self.up_blocks, reversed(skips)):
            h = up(h, skip, cond)

        h = self.out_norm(h)

        h = h[:, P : P + L, :]
        if h.size(1) != L:
            if h.size(1) > L:
                h = h[:, :L, :]
            else:
                pad = torch.zeros(B, L - h.size(1), D, device=h.device, dtype=h.dtype)
                h = torch.cat([h, pad], dim=1)

        return h


    def q_sample(
        self,
        x0: torch.Tensor,           # (B, L, D)  czyste osadzenia
        t: torch.Tensor,            # (B,)       int 1..T
        noise: torch.Tensor = None,
    ) -> torch.Tensor:
        """
        Dodaje szum Gaussowski zgodnie z cosinusowym harmonogramem:
            z_t = √ā_t · z_0 + √(1-ā_t) · ε
        """
        if noise is None:
            noise = torch.randn_like(x0)
        idx = (t - 1).clamp(0, self.T - 1)
        sqrt_ab  = self.sqrt_alphas_bar[idx].view(-1, 1, 1)
        sqrt_1mb = self.sqrt_one_minus_alphas_bar[idx].view(-1, 1, 1)
        return sqrt_ab * x0 + sqrt_1mb * noise


    def compute_loss(
        self,
        code_ids: torch.Tensor,    # (B, L)  dyskretne tokeny kodu
        prompt_ids: torch.Tensor,  # (B, P)  dyskretne tokeny promptu
    ) -> torch.Tensor:
        """
        Pełny krok treningowy wewnątrz modelu:
          1. Losuje t ∈ {1, …, T}
          2. Szumi osadzenia kodu: z_t = q_sample(z_0, t)
          3. Przepuszcza z_t przez U-Net → z_0_pred
          4. Liczy MSE(z_0_pred, z_0) z maskowaniem paddingów

        MSE na osadzeniach (x0-prediction) jest stabilniejsze niż
        predykcja szumu przy krótkich sekwencjach tekstowych.
        """
        B, L = code_ids.shape
        t = torch.randint(1, self.T + 1, (B,), device=code_ids.device)

        with torch.no_grad():
            x0 = self.token_embedding(code_ids)            # (B, L, D)

        noise = torch.randn_like(x0)
        z_t   = self.q_sample(x0, t, noise)

        z0_pred = self.forward(z_t, prompt_ids, t)

        # MSE z maskowaniem tokenów padding
        pad_mask = (code_ids != self.pad_token_id).float().unsqueeze(-1)  # (B, L, 1)
        loss = ((z0_pred - x0.detach()) ** 2 * pad_mask).sum() / pad_mask.sum().clamp(min=1)
        return loss


    def embedding_rounding(self, z0: torch.Tensor) -> torch.Tensor:
        """
        Mapuje ciągłe wektory z_0 na dyskretne tokeny przez cosine similarity
        z macierzą wagową warstwy Embedding, a następnie argmax.

            token_ids = argmax_v  [cos_sim(z_0, e_v)]

        Zwraca: (B, L) tensor indeksów tokenów.
        """
        W     = self.token_embedding.weight                # (V, D)
        W_n   = F.normalize(W,  dim=-1)                   # (V, D)
        z_n   = F.normalize(z0, dim=-1)                   # (B, L, D)
        sim   = torch.einsum("bld,vd->blv", z_n, W_n)    # (B, L, V)
        return sim.argmax(dim=-1)                          # (B, L)


    @torch.no_grad()
    def generate(
        self,
        prompt_ids: torch.Tensor,
        code_len: int = None,
        steps: int = 50,
        device: str = "cuda",
        eos_token_id: int = None,  # zachowany dla kompatybilności z train.py
    ) -> torch.Tensor:
        """
        Odszumia z_T → z_0 krokami DDPM (x0-prediction + posterior step),
        a następnie mapuje z_0 na tokeny przez Embedding Rounding.
        Zwraca: (1, L) tensor dyskretnych indeksów tokenów.
        """
        if prompt_ids.dim() == 1:
            prompt_ids = prompt_ids.unsqueeze(0)
        prompt_ids = prompt_ids.to(device)

        if code_len is None:
            code_len = max(self.max_seq_len - prompt_ids.size(1), 1)

        # Startujemy od czystego szumu gaussowskiego (z_T)
        z = torch.randn(1, code_len, self.hidden_dim, device=device)

        # Subsample T kroków równomiernie (np. T=1000 → steps=50)
        timesteps = torch.linspace(self.T, 1, steps, dtype=torch.long, device=device)

        for i, t_val in enumerate(timesteps):
            t_batch = t_val.unsqueeze(0)                   # (1,)

            # U-Net przewiduje czyste z_0 z zaszumionego z_t
            z0_pred = self.forward(z, prompt_ids, t_batch)

            # Indeks bieżącego kroku w harmonogramie
            t_idx = (t_val - 1).clamp(0, self.T - 1).item()
            sqrt_ab  = self.sqrt_alphas_bar[t_idx]
            sqrt_1mb = self.sqrt_one_minus_alphas_bar[t_idx]

            eps_pred = (z - sqrt_ab * z0_pred) / sqrt_1mb.clamp(min=1e-8)

            if i < len(timesteps) - 1:


                t_prev_idx = (timesteps[i + 1] - 1).clamp(0, self.T - 1).item()
                sqrt_ab_p  = self.sqrt_alphas_bar[t_prev_idx]
                sqrt_1mb_p = self.sqrt_one_minus_alphas_bar[t_prev_idx]
                z = sqrt_ab_p * z0_pred + sqrt_1mb_p * eps_pred
            else:
                z = z0_pred

        # Zaokrąglanie osadzeń → dyskretne tokeny
        token_ids = self.embedding_rounding(z)

        if eos_token_id is not None:
            eos_pos = (token_ids[0] == eos_token_id).nonzero(as_tuple=False)
            if eos_pos.numel() > 0:
                cut = int(eos_pos[0].item()) + 1
                token_ids = token_ids[:, :cut]

        return token_ids
