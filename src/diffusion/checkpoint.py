from __future__ import annotations

from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class VocabAdaptation:
    state_dict: dict[str, torch.Tensor]
    changed: bool
    source_vocab_size: int
    target_vocab_size: int
    legacy_mask_token_id: int | None


def adapt_state_dict_to_tokenizer(
    state_dict: dict[str, torch.Tensor],
    *,
    target_vocab_size: int,
    pad_token_id: int,
    mask_token_id: int,
    eos_token_id: int | None,
) -> VocabAdaptation:
    source_vocab_size = int(state_dict["token_embedding.weight"].shape[0])
    if source_vocab_size == target_vocab_size:
        return VocabAdaptation(
            state_dict=state_dict,
            changed=False,
            source_vocab_size=source_vocab_size,
            target_vocab_size=target_vocab_size,
            legacy_mask_token_id=None,
        )

    if source_vocab_size > target_vocab_size:
        raise ValueError(
            f"Checkpoint vocab ({source_vocab_size}) is larger than tokenizer vocab "
            f"({target_vocab_size}); refusing to truncate model weights."
        )

    legacy_mask_token_id = source_vocab_size - 1 if mask_token_id >= source_vocab_size else None
    adapted = {}

    for key, tensor in state_dict.items():
        if not _is_vocab_tensor(key, tensor, source_vocab_size):
            adapted[key] = tensor
            continue

        expanded = _expand_vocab_tensor(tensor, target_vocab_size)
        expanded[:source_vocab_size] = tensor

        if eos_token_id is not None and 0 <= eos_token_id < source_vocab_size:
            expanded[pad_token_id] = tensor[eos_token_id]

        if legacy_mask_token_id is not None and 0 <= legacy_mask_token_id < source_vocab_size:
            expanded[mask_token_id] = tensor[legacy_mask_token_id]

        adapted[key] = expanded

    return VocabAdaptation(
        state_dict=adapted,
        changed=True,
        source_vocab_size=source_vocab_size,
        target_vocab_size=target_vocab_size,
        legacy_mask_token_id=legacy_mask_token_id,
    )


def _is_vocab_tensor(key: str, tensor: torch.Tensor, source_vocab_size: int) -> bool:
    return (
        key in {"token_embedding.weight", "lm_head.weight", "lm_head.bias"}
        and tensor.size(0) == source_vocab_size
    )


def _expand_vocab_tensor(tensor: torch.Tensor, target_vocab_size: int) -> torch.Tensor:
    new_shape = (target_vocab_size, *tensor.shape[1:])
    expanded = tensor.new_zeros(new_shape)
    if tensor.ndim > 1:
        expanded[:] = tensor.mean(dim=0, keepdim=True)
    return expanded
