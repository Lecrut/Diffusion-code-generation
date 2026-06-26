import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

@torch.jit.script
def compute_soft_dtw(D: torch.Tensor, gamma: float) -> torch.Tensor:
    B, N, M = D.shape
    
    R = torch.full((B, N + 1, M + 1), float('inf'), device=D.device, dtype=D.dtype)
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


class CalculateLoss(nn.Module):
    def __init__(self, gamma=1.0, ce_weight=1.0, dtw_weight=0.1, embedding_matrix=None):
        super().__init__()
        self.gamma = gamma
        self.ce_weight = ce_weight
        self.dtw_weight = dtw_weight
        self.embedding_matrix = embedding_matrix

    def _pairwise_euclidean_distance(self, x, y):
        x_norm = (x ** 2).sum(dim=-1, keepdim=True)
        y_norm = (y ** 2).sum(dim=-1).unsqueeze(1)
        dist = x_norm + y_norm - 2.0 * torch.bmm(x, y.transpose(1, 2))
        return torch.clamp(dist, min=0.0)

    def forward(self, full_logits, masked_logits, masked_targets, ast_embeddings=None):
        if masked_targets.numel() > 0:
            ce_loss = F.cross_entropy(masked_logits, masked_targets)
        else:
            ce_loss = torch.tensor(0.0, device=full_logits.device, requires_grad=True)

        # 2. Jeśli nie liczymy DTW, zwracamy samo CE i urywamy obliczenia
        if ast_embeddings is None or self.dtw_weight == 0.0:
            return ce_loss, ce_loss, torch.tensor(0.0, device=full_logits.device)

        probs = F.softmax(full_logits, dim=-1) 
        
        expected_repr = torch.matmul(probs, self.embedding_matrix)

        dist_matrix = self._pairwise_euclidean_distance(expected_repr, ast_embeddings)
        dtw_costs = compute_soft_dtw(dist_matrix, self.gamma)
        dtw_loss = dtw_costs.mean()

        total_loss = (self.ce_weight * ce_loss) + (self.dtw_weight * dtw_loss)

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

    for row in range(x_0.size(0)):
        row_mask = target_mask[row]
        token_count = int(row_mask.sum().item())
        if token_count == 0:
            continue

        row_logits = masked_logits[logit_offset : logit_offset + token_count]
        logit_offset += token_count

        group_id = int(group_ids[row].detach().cpu().item())
        current_len = int(code_lens[row].detach().cpu().item())
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
