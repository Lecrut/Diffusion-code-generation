import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import os

@torch.jit.script
def compute_soft_dtw(D: torch.Tensor, gamma: float) -> torch.Tensor:
    # Perform DTW in float32 for numerical stability
    D = D.float()
    B, N, M = D.shape
    
    R = torch.full((B, N + 1, M + 1), float('inf'), device=D.device, dtype=torch.float32)
    R[:, 0, 0] = 0.0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            r_diag = R[:, i-1, j-1]
            r_up   = R[:, i-1, j]
            r_left = R[:, i, j-1]
            
            stacked = torch.stack([r_diag, r_up, r_left], dim=-1)
            soft_min = -gamma * torch.logsumexp(-stacked / gamma, dim=-1)
            
            R[:, i, j] = D[:, i-1, j-1] + soft_min

    return R[:, N, M]


@torch.jit.script
def compute_soft_dtw_batched(
    distances: torch.Tensor,
    gamma: float,
    code_lengths: torch.Tensor,
    ast_lengths: torch.Tensor,
) -> torch.Tensor:
    distances = distances.float()

    batch_size = distances.size(0)
    code_size = distances.size(1)
    ast_size = distances.size(2)

    table = torch.full(
        (batch_size, code_size + 1, ast_size + 1),
        float("inf"),
        device=distances.device,
        dtype=torch.float32,
    )
    table[:, 0, 0] = 0.0

    for i in range(1, code_size + 1):
        for j in range(1, ast_size + 1):
            previous = torch.stack(
                (
                    table[:, i - 1, j - 1],
                    table[:, i - 1, j],
                    table[:, i, j - 1],
                ),
                dim=-1,
            )

            soft_minimum = -gamma * torch.logsumexp(
                -previous / gamma,
                dim=-1,
            )

            table[:, i, j] = (
                distances[:, i - 1, j - 1]
                + soft_minimum
            )

    batch_indices = torch.arange(
        batch_size,
        device=distances.device,
    )

    return table[
        batch_indices,
        code_lengths,
        ast_lengths,
    ]


class CalculateLoss(nn.Module):
    def __init__(
        self,
        gamma=1.0,
        ce_weight=1.0,
        dtw_weight=0.1,
        embedding_matrix=None,
        max_dtw_code_len: int = 64,
        max_dtw_ast_len: int = 64,
    ):
        super().__init__()
        if gamma < 1e-6:
            raise ValueError(f"gamma must be strictly positive and >= 1e-6, got {gamma}")
        self.gamma = gamma
        self.ce_weight = ce_weight
        self.dtw_weight = dtw_weight
        self.max_dtw_code_len = int(max_dtw_code_len)
        self.max_dtw_ast_len = int(max_dtw_ast_len)
        # Keep a direct reference to the model token embedding without registering
        # a duplicate loss_fn parameter/state_dict key.
        object.__setattr__(self, "embedding_matrix", embedding_matrix)

    def _pairwise_dist_2d(self, x, y):
        # Compute squared Euclidean distance: ||x - y||^2 = ||x||^2 + ||y||^2 - 2 * x @ y^T
        x_norm = (x ** 2).sum(dim=-1, keepdim=True)
        y_norm = (y ** 2).sum(dim=-1).unsqueeze(0)
        dist = x_norm + y_norm - 2.0 * torch.matmul(x, y.transpose(0, 1))
        return torch.clamp(dist, min=0.0, max=1e5)

    @staticmethod
    def _pairwise_dist_batch(
        x: torch.Tensor,
        y: torch.Tensor,
    ) -> torch.Tensor:
        x_norm = (x * x).sum(dim=-1, keepdim=True)
        y_norm = (y * y).sum(dim=-1).unsqueeze(1)

        cross = torch.bmm(
            x,
            y.transpose(1, 2),
        )

        return (x_norm + y_norm - 2.0 * cross).clamp(
            min=0.0,
            max=1e5,
        )

    @staticmethod
    def _downsample_sequence(seq: torch.Tensor, length: int, max_length: int) -> tuple[torch.Tensor, int]:
        length = min(int(length), int(seq.size(0)))
        if length <= 0:
            return seq[:0], 0
        seq = seq[:length]
        if max_length <= 0 or length <= max_length:
            return seq, length
        indices = torch.linspace(
            0,
            length - 1,
            steps=int(max_length),
            device=seq.device,
        ).round().long()
        return seq.index_select(0, indices), int(indices.numel())

    @staticmethod
    def _downsample_batch(
        sequences: torch.Tensor,
        lengths: torch.Tensor,
        max_length: int,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        batch_size, sequence_size, embedding_size = sequences.shape

        output_size = (
            sequence_size
            if max_length <= 0
            else min(sequence_size, int(max_length))
        )

        lengths = lengths.to(
            device=sequences.device,
            dtype=torch.long,
        ).clamp(min=0, max=sequence_size)

        sampled_lengths = lengths.clamp(max=output_size)

        positions = torch.arange(
            output_size,
            device=sequences.device,
            dtype=torch.long,
        ).unsqueeze(0)

        denominator = (sampled_lengths - 1).clamp_min(1).unsqueeze(1)
        source_span = (lengths - 1).clamp_min(0).unsqueeze(1)

        indices = torch.round(
            positions.float()
            * source_span.float()
            / denominator.float()
        ).long()

        valid_positions = positions < sampled_lengths.unsqueeze(1)
        indices = torch.where(
            valid_positions,
            indices,
            torch.zeros_like(indices),
        )

        gather_indices = indices.unsqueeze(-1).expand(
            batch_size,
            output_size,
            embedding_size,
        )

        sampled = sequences.gather(1, gather_indices)
        return sampled, sampled_lengths

    def forward(
        self,
        full_logits=None,
        masked_logits=None,
        masked_targets=None,
        ast_embeddings=None,
        code_lengths=None,
        ast_lengths=None,
        dtw_weight=None,
        expected_repr=None,
        ce_loss=None,
    ):
        if ce_loss is not None:
            pass
        elif masked_targets is not None and masked_targets.numel() > 0:
            ce_loss = F.cross_entropy(masked_logits, masked_targets)
        else:
            dev = masked_logits.device if masked_logits is not None else (expected_repr.device if expected_repr is not None else (ast_embeddings.device if ast_embeddings is not None else torch.device("cpu")))
            ce_loss = torch.tensor(0.0, device=dev, requires_grad=True)

        active_dtw_weight = dtw_weight if dtw_weight is not None else self.dtw_weight

        # Weight condition fix to avoid GPU-CPU synchronization (don't convert CUDA tensor to Python boolean)
        skip_dtw = (
            ast_embeddings is None
            or code_lengths is None
            or ast_lengths is None
        )

        if isinstance(active_dtw_weight, (float, int)):
            skip_dtw = skip_dtw or active_dtw_weight == 0.0

        if skip_dtw:
            dev = masked_logits.device if masked_logits is not None else (expected_repr.device if expected_repr is not None else (ast_embeddings.device if ast_embeddings is not None else torch.device("cpu")))
            return ce_loss, ce_loss, torch.tensor(0.0, device=dev)

        if expected_repr is None:
            assert full_logits is not None, "Either full_logits or expected_repr must be provided"
            assert full_logits.ndim == 3, f"Expected 3D full_logits [B, N, V], got {full_logits.shape}"
            # Softmax over logits to get continuous probability distribution
            probs = F.softmax(full_logits, dim=-1)
            
            assert self.embedding_matrix is not None, "embedding_matrix must be provided to CalculateLoss to compute expected representations"
            # Differentiable expected token representation
            expected_repr = torch.matmul(probs, self.embedding_matrix)

        assert expected_repr.ndim == 3, f"expected_repr must be 3D [B, N, E], got {expected_repr.shape}"
        assert ast_embeddings.ndim == 3, f"Expected 3D ast_embeddings [B, M, E], got {ast_embeddings.shape}"
        assert expected_repr.size(-1) == ast_embeddings.size(-1), f"Embedding dimensions do not match: expected_repr={expected_repr.shape}, ast_embeddings={ast_embeddings.shape}"
        assert ast_embeddings.size(1) > 1 or (ast_lengths == 1).all(), f"AST is single-node or unexpectedly pooled: ast_embeddings={ast_embeddings.shape}"

        code_sequences, sampled_code_lengths = self._downsample_batch(
            expected_repr,
            code_lengths,
            self.max_dtw_code_len,
        )

        ast_sequences, sampled_ast_lengths = self._downsample_batch(
            ast_embeddings,
            ast_lengths,
            self.max_dtw_ast_len,
        )

        distance_matrices = self._pairwise_dist_batch(
            code_sequences,
            ast_sequences,
        )

        dtw_costs = compute_soft_dtw_batched(
            distance_matrices,
            float(self.gamma),
            sampled_code_lengths,
            sampled_ast_lengths,
        )

        normalizers = (
            sampled_code_lengths + sampled_ast_lengths
        ).clamp_min(1).float()

        valid_samples = (
            (sampled_code_lengths > 0)
            & (sampled_ast_lengths > 0)
        )

        normalized_costs = torch.where(
            valid_samples,
            dtw_costs / normalizers,
            torch.zeros_like(dtw_costs),
        )

        dtw_loss = normalized_costs.mean()

        # Debugging NaN/Inf check (disabled on hot path to avoid GPU sync)
        if os.environ.get("DETAILED_DEBUG_DTW", "0") == "1":
            if not torch.isfinite(dtw_loss).item():
                raise ValueError("DTW loss contains NaN or Inf.")

        total_loss = (self.ce_weight * ce_loss) + (active_dtw_weight * dtw_loss)

        return total_loss, ce_loss, dtw_loss


def aligned_multi_reference_cross_entropy(
    masked_logits: torch.Tensor,
    x_0: torch.Tensor,
    x_t: torch.Tensor,
    target_mask: torch.Tensor,
    code_lens: torch.Tensor,
    group_ids: torch.Tensor,
    reference_code_ids,
    reference_code_lens,
    group_ref_offsets,
    *,
    max_refs_per_group: int = 0,
    reduction: str = "mean",
) -> torch.Tensor:
    """Cross entropy against the best visible-compatible same-length reference."""
    if reduction not in {"mean", "sum"}:
        raise ValueError(f"Unsupported reduction: {reduction}")
    if masked_logits.numel() == 0:
        return masked_logits.new_zeros(())

    device = masked_logits.device
    total_loss = masked_logits.new_zeros(())
    total_tokens = 0
    logit_offset = 0

    offsets = np.asarray(group_ref_offsets)
    ref_lens_all = np.asarray(reference_code_lens)

    # GPU-to-CPU optimization to prevent repeated GPU-CPU synchronization stalls (Cause 13)
    token_counts = target_mask.sum(dim=1).cpu().tolist()
    group_ids_cpu = group_ids.cpu().tolist()
    code_lens_cpu = code_lens.cpu().tolist()

    for row in range(x_0.size(0)):
        row_mask = target_mask[row]
        token_count = token_counts[row]
        if token_count == 0:
            continue

        row_logits = masked_logits[logit_offset : logit_offset + token_count]
        logit_offset += token_count

        group_id = int(group_ids_cpu[row])
        current_len = int(code_lens_cpu[row])
        fallback_ref = x_0[row].unsqueeze(0)
        refs = fallback_ref

        if 0 <= group_id < len(offsets) - 1:
            start = int(offsets[group_id])
            end = int(offsets[group_id + 1])
            if max_refs_per_group and max_refs_per_group > 0:
                end = min(end, start + int(max_refs_per_group))

            if end > start:
                ref_lens_np = ref_lens_all[start:end]
                same_len_np = ref_lens_np == current_len
                if same_len_np.any():
                    refs_np = np.asarray(reference_code_ids[start:end][same_len_np], dtype=np.int64)
                    ref_tensor = torch.as_tensor(refs_np, device=device, dtype=torch.long)
                    visible_mask = ~row_mask
                    if visible_mask.any():
                        compatible = (ref_tensor[:, visible_mask] == x_t[row, visible_mask]).all(dim=1)
                        ref_tensor = ref_tensor[compatible]
                    if ref_tensor.numel() > 0:
                        refs = torch.cat([ref_tensor, fallback_ref], dim=0)

        log_probs = F.log_softmax(row_logits, dim=-1)
        candidate_targets = refs[:, row_mask]
        expanded_log_probs = log_probs.unsqueeze(0).expand(candidate_targets.size(0), -1, -1)
        candidate_losses = -expanded_log_probs.gather(
            dim=2,
            index=candidate_targets.unsqueeze(-1),
        ).squeeze(-1).sum(dim=1)
        total_loss = total_loss + candidate_losses.min()
        total_tokens += token_count

    if reduction == "sum":
        return total_loss
    return total_loss / max(total_tokens, 1)
