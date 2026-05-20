from __future__ import annotations

import argparse
from pathlib import Path
import sys

import torch

repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from src.diffusion.model import LocalConvDiffCoder
from src.tokenizer import CodeTokenizer


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Count parameters for LocalConvDiffCoder.")
    parser.add_argument("--hidden-dim", type=int, default=256)
    parser.add_argument("--num-blocks", type=int, default=4)
    parser.add_argument("--max-prompt-len", type=int, default=96)
    parser.add_argument("--max-code-len", type=int, default=1024)
    return parser


def count_params(model: torch.nn.Module) -> tuple[int, int, int]:
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    frozen = total - trainable
    return total, trainable, frozen


def main() -> None:
    args = build_arg_parser().parse_args()

    tokenizer = CodeTokenizer()
    model = LocalConvDiffCoder(
        vocab_size=tokenizer.vocab_size,
        mask_token_id=tokenizer.mask_token_id,
        pad_token_id=tokenizer.pad_token_id,
        hidden_dim=args.hidden_dim,
        num_blocks=args.num_blocks,
        max_seq_len=args.max_prompt_len + args.max_code_len,
    )

    total, trainable, frozen = count_params(model)
    print(f"Total params: {total:,}")
    print(f"Trainable params: {trainable:,}")
    print(f"Frozen params: {frozen:,}")


if __name__ == "__main__":
    main()
