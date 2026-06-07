import torch
import torch.nn as nn
import torch.nn.functional as F

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
        if ast_embeddings is None or self.embedding_matrix is None or self.dtw_weight == 0.0:
            return ce_loss, ce_loss, torch.tensor(0.0, device=full_logits.device)

        probs = F.softmax(full_logits, dim=-1) 
        
        expected_repr = torch.matmul(probs, self.embedding_matrix)

        dist_matrix = self._pairwise_euclidean_distance(expected_repr, ast_embeddings)
        dtw_costs = compute_soft_dtw(dist_matrix, self.gamma)
        dtw_loss = dtw_costs.mean()

        total_loss = (self.ce_weight * ce_loss) + (self.dtw_weight * dtw_loss)

        return total_loss, ce_loss, dtw_loss
