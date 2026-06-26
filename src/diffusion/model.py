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
    def __init__(self, dim, kernel_size=5, dilation=1, dropout=0.0):
        super().__init__()
        # padding tak dobrany, by zachować tę samą długość wyjścia jak wejścia
        padding = ((kernel_size - 1) // 2) * dilation
        self.conv = nn.Conv1d(dim, dim, kernel_size, padding=padding, dilation=dilation)
        self.ln = AdaLN(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, dim * 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(dim * 2, dim)
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, t_emb):
        res = x
        x = x.transpose(1, 2)
        x = self.conv(x).transpose(1, 2)
        x = self.ln(x, t_emb)
        x = self.dropout(x)
        x = x + res
        
        # Refinement (MLP)
        x = x + self.dropout(self.mlp(self.ln(x, t_emb)))
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
        dropout=0.0,
    ):
        super().__init__()
        self.vocab_size = vocab_size
        self.mask_token_id = mask_token_id
        self.pad_token_id = pad_token_id
        self.max_seq_len = max_seq_len
        
        self.token_embedding = nn.Embedding(vocab_size, hidden_dim)
        self.pos_emb = nn.Parameter(torch.zeros(1, max_seq_len, hidden_dim))
        self.embedding_dropout = nn.Dropout(dropout)
                
        self.time_mlp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        self.blocks = nn.ModuleList([
            CNNBlock(
                hidden_dim,
                kernel_size=5 + (i * 2),
                dilation=(dilation_factor ** i),
                dropout=dropout,
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


    def forward_features(self, x, prompt_ids, t):
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
        x_emb = self.embedding_dropout(x_emb)


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
        return x_out[:, prompt_len:, :]

    def forward(self, x, prompt_ids, t):
        code_features = self.forward_features(x, prompt_ids, t)
        return self.lm_head(self.ln_final(code_features))

    def forward_masked_logits(self, x, prompt_ids, t, code_mask):
        code_features = self.forward_features(x, prompt_ids, t)
        masked_features = code_features[code_mask]
        return self.lm_head(self.ln_final(masked_features))

    def _prepare_generation_logits(self, logits, eos_token_id=None, forbidden_token_ids=None):
        logits = logits.clone()
        logits[..., self.mask_token_id] = -torch.inf
        if self.pad_token_id is not None and self.pad_token_id != eos_token_id:
            logits[..., self.pad_token_id] = -torch.inf
        for token_id in forbidden_token_ids or ():
            token_id = int(token_id)
            if token_id != eos_token_id:
                logits[..., token_id] = -torch.inf
        return logits

    def masked_cross_entropy(
        self,
        x,
        prompt_ids,
        t,
        code_mask,
        targets,
        *,
        reduction="mean",
        chunk_size=0,
    ):
        code_features = self.forward_features(x, prompt_ids, t)
        masked_features = self.ln_final(code_features[code_mask])
        if masked_features.numel() == 0:
            return masked_features.new_zeros(())

        if chunk_size is None or chunk_size <= 0 or masked_features.size(0) <= chunk_size:
            logits = self.lm_head(masked_features)
            return F.cross_entropy(logits, targets, reduction=reduction)

        loss_sum = masked_features.new_zeros((), dtype=torch.float32)
        for start in range(0, masked_features.size(0), int(chunk_size)):
            end = min(start + int(chunk_size), masked_features.size(0))
            logits = self.lm_head(masked_features[start:end])
            loss_sum = loss_sum + F.cross_entropy(logits, targets[start:end], reduction="sum")

        if reduction == "sum":
            return loss_sum
        if reduction == "mean":
            return loss_sum / max(int(targets.numel()), 1)
        raise ValueError(f"Unsupported reduction: {reduction}")

    @torch.no_grad()
    def generate(
        self,
        prompt_ids,
        steps=50,
        device="cuda",
        eos_token_id=None,
        code_len=None,
        forbidden_token_ids=None,
        decoding_strategy="standard",
        remask_confidence_threshold=0.55,
        max_remask_fraction_per_step=0.10,
        max_remasks_per_token=2,
        remask_cooldown_steps=1,
        disable_remasking_last_n_steps=2,
        return_telemetry=False,
        # FIX (Cause 16): temperature scheduling – starts high to diversify
        # the initial all-mask prediction, anneals to 1.0 for final steps.
        initial_temperature: float = 1.0,
        temperature_anneal_steps: int = 0,
        sampling: bool = False,
    ):
        if prompt_ids.dim() == 1:
            prompt_ids = prompt_ids.unsqueeze(0)
        prompt_ids = prompt_ids.to(device)
        prompt_len = prompt_ids.size(1)
        if code_len is None:
            code_len = max(self.max_seq_len - prompt_len, 1)
        else:
            code_len = int(code_len)
            if code_len <= 0:
                raise ValueError("code_len must be a positive integer.")
            code_len = min(code_len, max(self.max_seq_len - prompt_len, 1))

        if decoding_strategy == "standard":
            return self._generate_standard(
                prompt_ids=prompt_ids,
                steps=steps,
                device=device,
                eos_token_id=eos_token_id,
                code_len=code_len,
                forbidden_token_ids=forbidden_token_ids,
                return_telemetry=return_telemetry,
                initial_temperature=initial_temperature,
                temperature_anneal_steps=temperature_anneal_steps,
                sampling=sampling,
            )
        if decoding_strategy in {"rcr", "t2m"}:
            return self._generate_running_confidence_remasking(
                prompt_ids=prompt_ids,
                steps=steps,
                device=device,
                eos_token_id=eos_token_id,
                code_len=code_len,
                forbidden_token_ids=forbidden_token_ids,
                remask_confidence_threshold=remask_confidence_threshold,
                max_remask_fraction_per_step=max_remask_fraction_per_step,
                max_remasks_per_token=max_remasks_per_token,
                remask_cooldown_steps=remask_cooldown_steps,
                disable_remasking_last_n_steps=disable_remasking_last_n_steps,
                return_telemetry=return_telemetry,
                initial_temperature=initial_temperature,
                temperature_anneal_steps=temperature_anneal_steps,
                sampling=sampling,
            )
        raise ValueError(f"Unknown decoding_strategy: {decoding_strategy}")

    @staticmethod
    def _step_temperature(step: int, initial_temperature: float, temperature_anneal_steps: int) -> float:
        """Linear temperature anneal from initial_temperature → 1.0 over the first temperature_anneal_steps steps."""
        if initial_temperature <= 1.0 or temperature_anneal_steps <= 0 or step >= temperature_anneal_steps:
            return 1.0
        progress = step / temperature_anneal_steps
        return initial_temperature + progress * (1.0 - initial_temperature)

    def _generate_standard(
        self,
        *,
        prompt_ids,
        steps,
        device,
        eos_token_id,
        code_len,
        forbidden_token_ids,
        return_telemetry,
        initial_temperature: float = 1.0,
        temperature_anneal_steps: int = 0,
        sampling: bool = False,
    ):
        seq = torch.full((1, code_len), self.mask_token_id, dtype=torch.long, device=device)
        telemetry = {
            "step": [],
            "avg_confidence": [],
            "committed_tokens": [],
            "remasked_tokens": [],
            "unresolved_mask_count": [],
            "target_mask_count": [],
            "actual_mask_count_before_prediction": [],
            "newly_resolved_tokens": [],
            "unchanged_masked_tokens": [],
            "min_retained_confidence": [],
        }

        for step in range(steps):
            t = torch.full((1,), (steps - step) / steps, device=device)
            logits = self.forward(seq, prompt_ids, t)
            logits = self._prepare_generation_logits(
                logits,
                eos_token_id=eos_token_id,
                forbidden_token_ids=forbidden_token_ids,
            )
            # FIX (Cause 16): apply temperature before softmax
            temp = self._step_temperature(step, initial_temperature, temperature_anneal_steps)
            if temp != 1.0:
                logits = logits / temp
            probs = F.softmax(logits, dim=-1)
            if sampling:
                B, L, V = probs.shape
                pred = torch.multinomial(probs.view(-1, V), num_samples=1).view(B, L)
                conf = torch.gather(probs, -1, pred.unsqueeze(-1)).squeeze(-1)
            else:
                conf, pred = probs.max(dim=-1)
            was_masked = seq == self.mask_token_id
            actual_mask_count_before = int(was_masked.sum().item())

            ratio = 1.0 - (step + 1) / steps
            num_to_mask = int(code_len * ratio)
            next_mask = torch.zeros_like(was_masked)

            if num_to_mask > 0:
                candidate_count = int(was_masked.sum().item())
                if candidate_count > 0:
                    scores = conf.masked_fill(~was_masked, 1.0)
                    _, mask_idx = torch.topk(scores, k=min(num_to_mask, candidate_count), largest=False)
                    next_mask[0, mask_idx[0]] = True

            next_seq = seq.clone()
            next_seq[was_masked] = pred[was_masked]
            next_seq[next_mask] = self.mask_token_id
            seq = next_seq
            unresolved = int((seq == self.mask_token_id).sum().item())
            newly_resolved = int((was_masked & ~next_mask).sum().item())
            unchanged_masked = int((was_masked & next_mask).sum().item())
            retained_conf = conf[~next_mask]
            telemetry["avg_confidence"].append(float(conf.mean().item()))
            telemetry["step"].append(step)
            telemetry["committed_tokens"].append(int(code_len - unresolved))
            telemetry["remasked_tokens"].append(0)
            telemetry["unresolved_mask_count"].append(unresolved)
            telemetry["target_mask_count"].append(num_to_mask)
            telemetry["actual_mask_count_before_prediction"].append(actual_mask_count_before)
            telemetry["newly_resolved_tokens"].append(newly_resolved)
            telemetry["unchanged_masked_tokens"].append(unchanged_masked)
            telemetry["min_retained_confidence"].append(
                float(retained_conf.min().item()) if retained_conf.numel() > 0 else 0.0
            )

        seq = self._cut_at_eos(seq, eos_token_id)
        telemetry["final_unresolved_mask_count"] = int((seq == self.mask_token_id).sum().item())
        if return_telemetry:
            return seq, telemetry
        return seq

    def _generate_running_confidence_remasking(
        self,
        *,
        prompt_ids,
        steps,
        device,
        eos_token_id,
        code_len,
        forbidden_token_ids,
        remask_confidence_threshold,
        max_remask_fraction_per_step,
        max_remasks_per_token,
        remask_cooldown_steps,
        disable_remasking_last_n_steps,
        return_telemetry,
        initial_temperature: float = 1.0,
        temperature_anneal_steps: int = 0,
        sampling: bool = False,
    ):
        seq = torch.full((1, code_len), self.mask_token_id, dtype=torch.long, device=device)
        previous_conf = torch.zeros((1, code_len), device=device)
        running_conf = torch.zeros((1, code_len), device=device)
        remask_counts = torch.zeros((1, code_len), device=device, dtype=torch.long)
        last_remask_step = torch.full((1, code_len), -10_000, device=device, dtype=torch.long)
        telemetry = {
            "step": [],
            "avg_confidence": [],
            "committed_tokens": [],
            "remasked_tokens": [],
            "unresolved_mask_count": [],
            "target_mask_count": [],
            "actual_mask_count_before_prediction": [],
            "newly_resolved_tokens": [],
            "unchanged_masked_tokens": [],
            "min_retained_confidence": [],
            "remask_count_per_position": None,
        }

        for step in range(steps):
            was_masked = seq == self.mask_token_id
            actual_mask_count_before = int(was_masked.sum().item())
            t = torch.full((1,), (steps - step) / steps, device=device)
            logits = self.forward(seq, prompt_ids, t)
            logits = self._prepare_generation_logits(
                logits,
                eos_token_id=eos_token_id,
                forbidden_token_ids=forbidden_token_ids,
            )
            # FIX (Cause 16): apply temperature before softmax
            temp = self._step_temperature(step, initial_temperature, temperature_anneal_steps)
            if temp != 1.0:
                logits = logits / temp
            probs = F.softmax(logits, dim=-1)
            if sampling:
                B, L, V = probs.shape
                pred = torch.multinomial(probs.view(-1, V), num_samples=1).view(B, L)
                conf = torch.gather(probs, -1, pred.unsqueeze(-1)).squeeze(-1)
            else:
                conf, pred = probs.max(dim=-1)

            if step == 0:
                running_conf = conf
            else:
                running_conf = (0.8 * running_conf) + (0.2 * conf)

            scheduled_mask_count = int(code_len * (1.0 - (step + 1) / steps))
            allow_remask = step < max(0, steps - disable_remasking_last_n_steps)
            next_mask = torch.zeros_like(was_masked)

            forced_remask = torch.zeros_like(was_masked)
            if allow_remask and scheduled_mask_count > 0:
                confidence_drop = previous_conf - conf
                cooldown_ok = (step - last_remask_step) > remask_cooldown_steps
                eligible_remask = (
                    (~was_masked)
                    & (remask_counts < max_remasks_per_token)
                    & cooldown_ok
                    & (
                        (conf < remask_confidence_threshold)
                        | (confidence_drop > 0.10)
                        | (conf < running_conf * 0.80)
                    )
                )
                max_step_remasks = int(max(1, round(code_len * max_remask_fraction_per_step)))
                max_step_remasks = min(max_step_remasks, scheduled_mask_count)
                candidate_count = int(eligible_remask.sum().item())
                if candidate_count > 0 and max_step_remasks > 0:
                    candidate_scores = conf.masked_fill(~eligible_remask, 1.0)
                    _, forced_idx = torch.topk(
                        candidate_scores,
                        k=min(candidate_count, max_step_remasks),
                        largest=False,
                    )
                    forced_remask[0, forced_idx[0]] = True
                    next_mask |= forced_remask

            remaining_mask_slots = scheduled_mask_count - int(next_mask.sum().item())
            if remaining_mask_slots > 0:
                candidates = was_masked & ~next_mask
                candidate_count = int(candidates.sum().item())
                if candidate_count > 0:
                    scores = conf.masked_fill(~candidates, 1.0)
                    _, low_idx = torch.topk(scores, k=min(remaining_mask_slots, candidate_count), largest=False)
                    next_mask[0, low_idx[0]] = True

            next_seq = seq.clone()
            next_seq[was_masked] = pred[was_masked]
            newly_remasked = next_mask & (~was_masked)
            if newly_remasked.any():
                remask_counts[newly_remasked] += 1
                last_remask_step[newly_remasked] = step
            next_seq[next_mask] = self.mask_token_id
            seq = next_seq
            previous_conf = conf

            unresolved = int(next_mask.sum().item())
            newly_resolved_count = int((was_masked & ~next_mask).sum().item())
            unchanged_masked_count = int((was_masked & next_mask).sum().item())
            retained_conf = conf[~next_mask]
            telemetry["avg_confidence"].append(float(conf.mean().item()))
            telemetry["step"].append(step)
            telemetry["committed_tokens"].append(int(code_len - unresolved))
            telemetry["remasked_tokens"].append(int(newly_remasked.sum().item()))
            telemetry["unresolved_mask_count"].append(unresolved)
            telemetry["target_mask_count"].append(scheduled_mask_count)
            telemetry["actual_mask_count_before_prediction"].append(actual_mask_count_before)
            telemetry["newly_resolved_tokens"].append(newly_resolved_count)
            telemetry["unchanged_masked_tokens"].append(unchanged_masked_count)
            telemetry["min_retained_confidence"].append(
                float(retained_conf.min().item()) if retained_conf.numel() > 0 else 0.0
            )

        seq = self._cut_at_eos(seq, eos_token_id)
        telemetry["final_unresolved_mask_count"] = int((seq == self.mask_token_id).sum().item())
        telemetry["remask_count_per_position"] = remask_counts[0].detach().cpu().tolist()
        if return_telemetry:
            return seq, telemetry
        return seq

    @staticmethod
    def _cut_at_eos(seq, eos_token_id):
        if eos_token_id is None:
            return seq
        eos_pos = (seq[0] == eos_token_id).nonzero(as_tuple=False)
        if eos_pos.numel() == 0:
            return seq
        cut = int(eos_pos[0].item()) + 1
        return seq[:, :cut]
