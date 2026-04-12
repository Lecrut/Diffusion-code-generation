from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn


@dataclass
class GenerationResult:
    full_token_ids: list[int]
    generated_token_ids: list[int]


class BasicDiffusionModel(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        mask_token_id: int,
        max_seq_len: int = 512,
        d_model: int = 128,
        num_heads: int = 4,
        num_layers: int = 2,
        dropout: float = 0.1,
        device: str = "cpu",
    ) -> None:
        super().__init__()
        self.vocab_size = vocab_size
        self.mask_token_id = mask_token_id
        self.max_seq_len = max_seq_len
        self.device = torch.device(device)

        self.token_embedding = nn.Embedding(vocab_size, d_model)
        self.position_embedding = nn.Embedding(max_seq_len, d_model)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=num_heads,
            dim_feedforward=d_model * 4,
            dropout=dropout,
            batch_first=True,
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.layer_norm = nn.LayerNorm(d_model)
        self.output_projection = nn.Linear(d_model, vocab_size)
        self.to(self.device)

    @staticmethod
    def resolve_mask_token_id(tokenizer) -> int:
        if tokenizer.mask_token_id is not None:
            return int(tokenizer.mask_token_id)
        if tokenizer.unk_token_id is not None:
            return int(tokenizer.unk_token_id)
        if tokenizer.eos_token_id is not None:
            return int(tokenizer.eos_token_id)
        if tokenizer.pad_token_id is not None:
            return int(tokenizer.pad_token_id)
        return 0

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        if input_ids.dim() != 2:
            raise ValueError("input_ids must have shape [batch_size, seq_len]")

        batch_size, seq_len = input_ids.shape
        if seq_len > self.max_seq_len:
            raise ValueError(
                f"Input sequence length {seq_len} exceeds max_seq_len {self.max_seq_len}."
            )

        positions = torch.arange(seq_len, device=input_ids.device).unsqueeze(0)
        positions = positions.expand(batch_size, seq_len)

        x = self.token_embedding(input_ids) + self.position_embedding(positions)
        x = self.encoder(x)
        x = self.layer_norm(x)
        return self.output_projection(x)

    def generate(
        self,
        condition_ids: list[int],
        generate_length: int = 64,
        steps: int = 8,
        temperature: float = 1.0,
        seed: int | None = 42,
    ) -> GenerationResult:
        if not condition_ids:
            raise ValueError("condition_ids must not be empty")
        if generate_length <= 0:
            raise ValueError("generate_length must be > 0")
        if steps <= 0:
            raise ValueError("steps must be > 0")

        if seed is not None:
            torch.manual_seed(seed)

        self.eval()
        condition = torch.tensor(condition_ids, dtype=torch.long, device=self.device)
        sequence = torch.cat(
            [
                condition,
                torch.full(
                    (generate_length,),
                    fill_value=self.mask_token_id,
                    dtype=torch.long,
                    device=self.device,
                ),
            ]
        )
        condition_len = int(condition.shape[0])

        for step_idx in range(steps):
            with torch.no_grad():
                logits = self(sequence.unsqueeze(0)).squeeze(0)
                logits = logits / max(temperature, 1e-6)
                probs = torch.softmax(logits, dim=-1)

            sampled_ids = torch.multinomial(probs, num_samples=1).squeeze(-1)
            confidence = probs.gather(1, sampled_ids.unsqueeze(-1)).squeeze(-1)

            gen_positions = torch.arange(condition_len, sequence.shape[0], device=self.device)
            masked_positions = gen_positions[sequence[gen_positions] == self.mask_token_id]
            if masked_positions.numel() == 0:
                break

            remaining_steps = steps - step_idx
            fill_count = max(1, int(masked_positions.numel() / remaining_steps))
            fill_count = min(fill_count, int(masked_positions.numel()))

            masked_confidence = confidence[masked_positions]
            _, fill_idx = torch.topk(masked_confidence, k=fill_count)
            selected_positions = masked_positions[fill_idx]
            sequence[selected_positions] = sampled_ids[selected_positions]

            generated_positions = gen_positions[sequence[gen_positions] != self.mask_token_id]
            if generated_positions.numel() > 0 and step_idx < steps - 1:
                keep_ratio = (step_idx + 1) / steps
                keep_count = max(1, int(generated_positions.numel() * keep_ratio))
                generated_conf = confidence[generated_positions]
                _, keep_idx = torch.topk(
                    generated_conf,
                    k=min(keep_count, int(generated_positions.numel())),
                )
                keep_positions = generated_positions[keep_idx]
                keep_mask = torch.zeros_like(generated_positions, dtype=torch.bool)
                for idx, pos in enumerate(generated_positions):
                    if torch.any(keep_positions == pos):
                        keep_mask[idx] = True

                remask_positions = generated_positions[~keep_mask]
                sequence[remask_positions] = self.mask_token_id

        full_ids = sequence.detach().cpu().tolist()
        return GenerationResult(
            full_token_ids=full_ids,
            generated_token_ids=full_ids[condition_len:],
        )
