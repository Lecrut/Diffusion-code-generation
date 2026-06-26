from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import torch


@dataclass(frozen=True)
class NoiseRegimeConfig:
    """One bounded component in the sequence-level mask probability mixture."""

    name: str
    low: float
    high: float
    weight: float
    alpha: float = 1.0
    beta: float = 1.0


@dataclass(frozen=True)
class MixtureMaskSamplerConfig:
    regimes: tuple[NoiseRegimeConfig, ...]
    seed: int | None = None

    def validate(self) -> None:
        if not self.regimes:
            raise ValueError("At least one noise regime is required.")
        total_weight = sum(regime.weight for regime in self.regimes)
        if abs(total_weight - 1.0) > 1e-5:
            raise ValueError(f"Noise regime weights must sum to 1.0, got {total_weight:.6f}.")
        for regime in self.regimes:
            if not (0.0 <= regime.low <= regime.high <= 1.0):
                raise ValueError(f"Invalid range for regime {regime.name}: [{regime.low}, {regime.high}].")
            if regime.weight < 0.0:
                raise ValueError(f"Regime {regime.name} has negative weight.")
            if regime.alpha <= 0.0 or regime.beta <= 0.0:
                raise ValueError(f"Regime {regime.name} beta parameters must be positive.")


@dataclass(frozen=True)
class MaskSamplerOutput:
    mask_prob: torch.Tensor
    regime_ids: torch.Tensor
    regime_names: tuple[str, ...]


class MixtureMaskSampler:
    """Samples one mask probability per sequence from a categorical bounded mixture."""

    def __init__(self, config: MixtureMaskSamplerConfig) -> None:
        config.validate()
        self.config = config
        self.regime_names = tuple(regime.name for regime in config.regimes)
        self._generators: dict[str, torch.Generator] = {}

    def sample(self, batch_size: int, device: torch.device | str) -> MaskSamplerOutput:
        device = torch.device(device)
        weights = torch.tensor([regime.weight for regime in self.config.regimes], device=device)
        lows = torch.tensor([regime.low for regime in self.config.regimes], device=device, dtype=torch.float32)
        highs = torch.tensor([regime.high for regime in self.config.regimes], device=device, dtype=torch.float32)
        alphas = torch.tensor([regime.alpha for regime in self.config.regimes], device=device, dtype=torch.float32)
        betas = torch.tensor([regime.beta for regime in self.config.regimes], device=device, dtype=torch.float32)
        generator = None
        if self.config.seed is not None:
            key = str(device)
            generator = self._generators.get(key)
            if generator is None:
                generator = torch.Generator(device=device)
                generator.manual_seed(int(self.config.seed))
                self._generators[key] = generator
        regime_ids = torch.multinomial(weights, batch_size, replacement=True, generator=generator)
        u = torch.rand(batch_size, device=device, generator=generator).clamp_(1e-6, 1.0 - 1e-6)
        alpha = alphas[regime_ids]
        beta = betas[regime_ids]
        low = lows[regime_ids]
        high = highs[regime_ids]
        shaped = (1.0 - (1.0 - u).pow(1.0 / beta)).pow(1.0 / alpha)
        mask_prob = low + shaped * (high - low)

        return MaskSamplerOutput(
            mask_prob=mask_prob,
            regime_ids=regime_ids,
            regime_names=self.regime_names,
        )


@dataclass(frozen=True)
class TopologyConfig:
    independent: float = 0.25
    block: float = 0.35
    prefix: float = 0.25
    truncated_suffix: float = 0.15
    block_lengths: tuple[int, ...] = (2, 4, 8)
    min_visible_prefix_fraction: float = 0.05
    max_visible_prefix_fraction: float = 0.75
    min_truncated_visible_tokens: int = 1
    # Above this mask probability, prefix/suffix topologies are suppressed so
    # the model cannot rely on visible anchors and must use the prompt.
    high_mask_independent_threshold: float = 0.80

    def validate(self) -> None:
        weights = [self.independent, self.block, self.prefix, self.truncated_suffix]
        total_weight = sum(weights)
        if abs(total_weight - 1.0) > 1e-5:
            raise ValueError(f"Topology weights must sum to 1.0, got {total_weight:.6f}.")
        if any(weight < 0.0 for weight in weights):
            raise ValueError("Topology weights must be non-negative.")
        if not self.block_lengths or any(length <= 0 for length in self.block_lengths):
            raise ValueError("Block lengths must be positive integers.")
        if not (0.0 <= self.min_visible_prefix_fraction <= self.max_visible_prefix_fraction < 1.0):
            raise ValueError("Prefix fractions must satisfy 0 <= min <= max < 1.")
        if self.min_truncated_visible_tokens < 0:
            raise ValueError("min_truncated_visible_tokens must be non-negative.")
        if not (0.0 <= self.high_mask_independent_threshold <= 1.0):
            raise ValueError("high_mask_independent_threshold must be in [0, 1].")


@dataclass(frozen=True)
class CorruptionOutput:
    input_ids: torch.Tensor
    target_mask: torch.Tensor
    topology_ids: torch.Tensor
    requested_mask_prob: torch.Tensor
    realized_mask_ratio: torch.Tensor
    eligible_counts: torch.Tensor
    masked_counts: torch.Tensor
    visible_prefix_fraction: torch.Tensor
    truncated_suffix_fraction: torch.Tensor
    block_length_ids: torch.Tensor
    topology_names: tuple[str, ...]
    block_lengths: tuple[int, ...]


class CodeCorruptor:
    """Applies sequence-level code corruption while protecting special tokens."""

    topology_names = ("independent", "block", "prefix", "truncated_suffix", "full")

    def __init__(
        self,
        *,
        mask_token_id: int,
        pad_token_id: int,
        protected_token_ids: Sequence[int],
        config: TopologyConfig,
    ) -> None:
        config.validate()
        self.mask_token_id = int(mask_token_id)
        self.pad_token_id = int(pad_token_id)
        self.protected_token_ids = tuple(sorted({int(token_id) for token_id in protected_token_ids}))
        self.config = config

    def eligible_mask(self, x: torch.Tensor) -> torch.Tensor:
        eligible = torch.ones_like(x, dtype=torch.bool)
        for token_id in self.protected_token_ids:
            eligible &= x != token_id
        return eligible

    def corrupt(self, x_0: torch.Tensor, mask_prob: torch.Tensor) -> CorruptionOutput:
        if x_0.dim() != 2:
            raise ValueError("x_0 must be a [batch, seq] tensor.")
        if mask_prob.dim() != 1 or mask_prob.size(0) != x_0.size(0):
            raise ValueError("mask_prob must be a [batch] tensor aligned with x_0.")

        device = x_0.device
        batch_size = x_0.size(0)
        x_t = x_0.clone()
        eligible = self.eligible_mask(x_0)
        eligible_counts = eligible.sum(dim=1).to(torch.long)
        requested_counts = torch.round(mask_prob * eligible_counts.float()).to(torch.long)
        requested_counts = torch.where(
            eligible_counts > 0,
            torch.minimum(requested_counts.clamp_min(1), eligible_counts),
            torch.zeros_like(requested_counts),
        )

        topology_weights = torch.tensor(
            [
                self.config.independent,
                self.config.block,
                self.config.prefix,
                self.config.truncated_suffix,
            ],
            device=device,
            dtype=torch.float32,
        )
        topology_ids = torch.multinomial(topology_weights, batch_size, replacement=True)

        # FIX (Cause 3/4): For high-mask samples, force independent topology so
        # the model cannot exploit visible prefix/suffix anchors and must rely
        # on the prompt instead.
        high_mask_rows = mask_prob >= self.config.high_mask_independent_threshold
        if high_mask_rows.any():
            # topology_id 0 = independent, 2 = prefix, 3 = truncated_suffix
            is_visible_topology = (topology_ids == 2) | (topology_ids == 3)
            force_independent = high_mask_rows & is_visible_topology
            if force_independent.any():
                topology_ids = topology_ids.clone()
                topology_ids[force_independent] = 0  # independent

        block_lengths_tensor = torch.tensor(self.config.block_lengths, device=device, dtype=torch.long)

        visible_prefix_fraction = torch.zeros(batch_size, device=device, dtype=torch.float32)
        truncated_suffix_fraction = torch.zeros(batch_size, device=device, dtype=torch.float32)
        block_length_ids = torch.full((batch_size,), -1, device=device, dtype=torch.long)

        full_rows = (mask_prob >= 1.0 - 1e-6) & (eligible_counts > 0)
        target_mask = self._vectorized_non_block_mask(
            eligible=eligible,
            eligible_counts=eligible_counts,
            requested_counts=requested_counts,
            topology_ids=topology_ids,
            visible_prefix_fraction=visible_prefix_fraction,
            truncated_suffix_fraction=truncated_suffix_fraction,
        )
        if full_rows.any():
            target_mask[full_rows] = eligible[full_rows]
            topology_ids = topology_ids.clone()
            topology_ids[full_rows] = len(self.topology_names) - 1

        block_rows = ((topology_ids == 1) & ~full_rows).nonzero(as_tuple=False).flatten()
        for row_tensor in block_rows:
            row = int(row_tensor.item())
            positions = eligible[row].nonzero(as_tuple=False).flatten()
            n_eligible = int(positions.numel())
            if n_eligible == 0:
                continue

            requested = int(requested_counts[row].item())
            selected, block_length_id = self._sample_blocks(
                eligible[row],
                positions,
                requested,
                block_lengths_tensor,
            )
            block_length_ids[row] = block_length_id

            if selected.numel() == 0:
                selected = positions[:1]
            target_mask[row, selected] = True

        x_t[target_mask] = self.mask_token_id
        masked_counts = target_mask.sum(dim=1).to(torch.long)
        realized = masked_counts.float() / eligible_counts.clamp_min(1).float()
        realized = torch.where(eligible_counts > 0, realized, torch.zeros_like(realized))

        return CorruptionOutput(
            input_ids=x_t,
            target_mask=target_mask,
            topology_ids=topology_ids,
            requested_mask_prob=mask_prob,
            realized_mask_ratio=realized,
            eligible_counts=eligible_counts,
            masked_counts=masked_counts,
            visible_prefix_fraction=visible_prefix_fraction,
            truncated_suffix_fraction=truncated_suffix_fraction,
            block_length_ids=block_length_ids,
            topology_names=self.topology_names,
            block_lengths=self.config.block_lengths,
        )

    def _vectorized_non_block_mask(
        self,
        *,
        eligible: torch.Tensor,
        eligible_counts: torch.Tensor,
        requested_counts: torch.Tensor,
        topology_ids: torch.Tensor,
        visible_prefix_fraction: torch.Tensor,
        truncated_suffix_fraction: torch.Tensor,
    ) -> torch.Tensor:
        batch_size, seq_len = eligible.shape
        device = eligible.device
        target_mask = torch.zeros_like(eligible, dtype=torch.bool)
        eligible_rank = eligible.long().cumsum(dim=1) - 1

        independent_rows = topology_ids == 0
        if independent_rows.any():
            counts = torch.where(independent_rows, requested_counts, torch.zeros_like(requested_counts))
            target_mask |= self._sample_random_mask(eligible, counts)

        prefix_rows = topology_ids == 2
        if prefix_rows.any():
            min_fraction = self.config.min_visible_prefix_fraction
            max_fraction = self.config.max_visible_prefix_fraction
            sampled_fraction = min_fraction + torch.rand(batch_size, device=device) * (max_fraction - min_fraction)
            visible_counts = torch.round(sampled_fraction * eligible_counts.float()).to(torch.long)
            visible_counts = torch.minimum(visible_counts, (eligible_counts - 1).clamp_min(0))
            visible_counts = torch.where(prefix_rows, visible_counts, torch.zeros_like(visible_counts))

            candidate_mask = eligible & (eligible_rank >= visible_counts.unsqueeze(1))
            candidate_counts = (eligible_counts - visible_counts).clamp_min(0)
            counts = torch.minimum(requested_counts, candidate_counts)
            counts = torch.where(prefix_rows & (candidate_counts > 0), counts.clamp_min(1), torch.zeros_like(counts))
            target_mask |= self._sample_random_mask(candidate_mask, counts)

            visible_prefix_fraction.copy_(
                torch.where(
                    prefix_rows & (eligible_counts > 0),
                    visible_counts.float() / eligible_counts.clamp_min(1).float(),
                    visible_prefix_fraction,
                )
            )

        suffix_rows = topology_ids == 3
        if suffix_rows.any():
            max_suffix = (eligible_counts - int(self.config.min_truncated_visible_tokens)).clamp_min(1)
            suffix_counts = torch.minimum(requested_counts, max_suffix)
            suffix_counts = torch.where(suffix_rows, suffix_counts, torch.zeros_like(suffix_counts))
            start_rank = eligible_counts - suffix_counts
            suffix_mask = eligible & (eligible_rank >= start_rank.unsqueeze(1))
            target_mask |= suffix_mask & suffix_rows.unsqueeze(1)
            truncated_suffix_fraction.copy_(
                torch.where(
                    suffix_rows & (eligible_counts > 0),
                    suffix_counts.float() / eligible_counts.clamp_min(1).float(),
                    truncated_suffix_fraction,
                )
            )

        return target_mask

    @staticmethod
    def _sample_random_mask(candidate_mask: torch.Tensor, counts: torch.Tensor) -> torch.Tensor:
        if not candidate_mask.any():
            return torch.zeros_like(candidate_mask, dtype=torch.bool)
        batch_size, seq_len = candidate_mask.shape
        scores = torch.rand((batch_size, seq_len), device=candidate_mask.device)
        scores = scores.masked_fill(~candidate_mask, -1.0)
        order = scores.argsort(dim=1, descending=True)
        ranks = torch.empty_like(order)
        rank_values = torch.arange(seq_len, device=candidate_mask.device).expand(batch_size, -1)
        ranks.scatter_(1, order, rank_values)
        return candidate_mask & (ranks < counts.unsqueeze(1))

    def deterministic_independent_mask(
        self,
        x_0: torch.Tensor,
        mask_prob: float,
        sample_ids: torch.Tensor,
        *,
        bin_index: int,
        seed: int,
    ) -> torch.Tensor:
        """Builds stable per-example masks for fixed-bin validation."""
        if sample_ids.dim() != 1 or sample_ids.size(0) != x_0.size(0):
            raise ValueError("sample_ids must be a [batch] tensor aligned with x_0.")

        device = x_0.device
        eligible = self.eligible_mask(x_0)
        target_mask = torch.zeros_like(x_0, dtype=torch.bool)
        for row in range(x_0.size(0)):
            positions = eligible[row].nonzero(as_tuple=False).flatten()
            n_eligible = int(positions.numel())
            if n_eligible == 0:
                continue
            target_count = int(round(float(mask_prob) * n_eligible))
            target_count = max(1, min(target_count, n_eligible))
            generator = torch.Generator(device=device)
            generator.manual_seed(stable_validation_seed(int(sample_ids[row].item()), bin_index, seed))
            order = torch.randperm(n_eligible, device=device, generator=generator)[:target_count]
            target_mask[row, positions[order]] = True
        return target_mask

    def _sample_independent(self, positions: torch.Tensor, count: int) -> torch.Tensor:
        order = torch.randperm(int(positions.numel()), device=positions.device)[:count]
        return positions[order]

    def _sample_prefix(self, positions: torch.Tensor, count: int) -> tuple[torch.Tensor, torch.Tensor]:
        n_eligible = int(positions.numel())
        if n_eligible <= 1:
            return positions[:1], torch.tensor(0.0, device=positions.device)

        min_visible = int(round(self.config.min_visible_prefix_fraction * n_eligible))
        max_visible = int(round(self.config.max_visible_prefix_fraction * n_eligible))
        min_visible = max(0, min(min_visible, n_eligible - 1))
        max_visible = max(min_visible, min(max_visible, n_eligible - 1))
        visible_count = int(
            torch.randint(
                low=min_visible,
                high=max_visible + 1,
                size=(1,),
                device=positions.device,
            ).item()
        )
        candidate_positions = positions[visible_count:]
        target_count = max(1, min(count, int(candidate_positions.numel())))
        selected = self._sample_independent(candidate_positions, target_count)
        prefix_fraction = torch.tensor(visible_count / n_eligible, device=positions.device, dtype=torch.float32)
        return selected, prefix_fraction

    def _sample_truncated_suffix(self, positions: torch.Tensor, count: int) -> tuple[torch.Tensor, torch.Tensor]:
        n_eligible = int(positions.numel())
        if n_eligible <= 1:
            return positions[-1:], torch.tensor(1.0, device=positions.device)

        max_suffix = max(1, n_eligible - self.config.min_truncated_visible_tokens)
        suffix_count = max(1, min(count, max_suffix))
        selected = positions[-suffix_count:]
        suffix_fraction = torch.tensor(suffix_count / n_eligible, device=positions.device, dtype=torch.float32)
        return selected, suffix_fraction

    def _sample_blocks(
        self,
        eligible_row: torch.Tensor,
        positions: torch.Tensor,
        count: int,
        block_lengths_tensor: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        device = positions.device
        block_length_id = torch.randint(
            low=0,
            high=int(block_lengths_tensor.numel()),
            size=(1,),
            device=device,
        )
        requested_block_len = int(block_lengths_tensor[block_length_id].item())
        selected_mask = torch.zeros_like(eligible_row, dtype=torch.bool)
        selected_count = 0
        attempts = 0
        max_attempts = max(16, count * 8)

        while selected_count < count and attempts < max_attempts:
            remaining = count - selected_count
            block_len = max(1, min(requested_block_len, remaining))
            valid_starts = self._valid_block_starts(eligible_row, selected_mask, block_len)
            if valid_starts.numel() == 0 and block_len > 1:
                block_len = 1
                valid_starts = self._valid_block_starts(eligible_row, selected_mask, block_len)
            if valid_starts.numel() == 0:
                break
            start = valid_starts[torch.randint(0, int(valid_starts.numel()), (1,), device=device)].item()
            selected_mask[start : start + block_len] = True
            selected_count += block_len
            attempts += 1

        selected = selected_mask.nonzero(as_tuple=False).flatten()
        if selected.numel() < count:
            missing = count - int(selected.numel())
            available = positions[~selected_mask[positions]]
            if available.numel() > 0:
                selected = torch.cat([selected, self._sample_independent(available, min(missing, int(available.numel())))])
        if selected.numel() > count:
            selected = selected[:count]
        return selected, block_length_id.squeeze(0)

    @staticmethod
    def _valid_block_starts(
        eligible_row: torch.Tensor,
        selected_mask: torch.Tensor,
        block_len: int,
    ) -> torch.Tensor:
        seq_len = int(eligible_row.numel())
        if block_len > seq_len:
            return torch.empty(0, device=eligible_row.device, dtype=torch.long)
        eligible_windows = eligible_row.unfold(0, block_len, 1)
        selected_windows = selected_mask.unfold(0, block_len, 1)
        valid = eligible_windows.all(dim=1) & ~selected_windows.any(dim=1)
        return valid.nonzero(as_tuple=False).flatten()


def stable_validation_seed(sample_id: int, bin_index: int, base_seed: int) -> int:
    value = int(base_seed) & 0x7FFFFFFFFFFFFFFF
    value ^= (int(sample_id) + 0x9E3779B97F4A7C15) & 0x7FFFFFFFFFFFFFFF
    value ^= ((int(bin_index) + 1) * 0xBF58476D1CE4E5B9) & 0x7FFFFFFFFFFFFFFF
    value = (value ^ (value >> 30)) * 0xBF58476D1CE4E5B9
    value = (value ^ (value >> 27)) * 0x94D049BB133111EB
    value = value ^ (value >> 31)
    return int(value & 0x7FFFFFFFFFFFFFFF)


def ratio_from_counts(numerator: torch.Tensor, denominator: torch.Tensor) -> torch.Tensor:
    return numerator.float() / denominator.clamp_min(1).float()
