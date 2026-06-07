from __future__ import annotations

import argparse
import ast
import json
import math
import re
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import torch

repo_root = Path(__file__).resolve().parents[1]
src_root = repo_root / "src"
for import_path in (repo_root, src_root):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from diffusion.checkpoint import adapt_state_dict_to_tokenizer
from diffusion.model import LocalConvDiffCoder
from tokenizer import CodeTokenizer


@dataclass
class SampleResult:
    index: int
    dataset_index: int
    instruction: str
    target_code: str
    generated_code: str
    compile_ok: bool
    compile_error: str
    parse_ok: bool
    generated_token_count: int
    generated_char_count: int
    target_char_count: int
    has_mask_token_id: bool
    has_pad_token_id: bool
    has_eos_token_id: bool
    eos_position: int | None
    elapsed_seconds: float


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate LocalConvDiffCoder generation from a checkpoint."
    )
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=repo_root / "checkpoints" / "diffcoder_best.pt",
        help="Checkpoint path to evaluate.",
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=repo_root / "data" / "dataset.csv",
        help="Dataset CSV with instruction and code columns.",
    )
    parser.add_argument("--num-samples", type=int, default=25)
    parser.add_argument("--steps", type=int, default=50)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--val-split", type=float, default=0.05)
    parser.add_argument("--dataset-fraction", type=float, default=1.0)
    parser.add_argument("--max-prompt-len", type=int, default=96)
    parser.add_argument("--max-code-len", type=int, default=512)
    parser.add_argument(
        "--max-code-lens",
        default="",
        help="Comma-separated max code lengths to evaluate, e.g. 128,256,512.",
    )
    parser.add_argument("--hidden-dim", type=int, default=None)
    parser.add_argument("--num-blocks", type=int, default=None)
    parser.add_argument("--dilation-factor", type=int, default=2)
    parser.add_argument(
        "--tokenizer",
        default="Qwen/Qwen2.5-Coder-7B",
        help="Tokenizer model id or local tokenizer snapshot path.",
    )
    parser.add_argument(
        "--device",
        choices=("auto", "cuda", "cpu"),
        default="auto",
        help="Device used for generation.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=repo_root / "reports",
        help="Directory for JSON and JSONL reports.",
    )
    parser.add_argument(
        "--prefix",
        default="generation_eval",
        help="Output filename prefix.",
    )
    return parser


def resolve_tokenizer_source(source: str) -> str:
    source_path = Path(source)
    if source_path.exists():
        return str(source_path)

    if "/" not in source:
        return source

    cache_root = Path.home() / ".cache" / "huggingface" / "hub"
    model_cache = cache_root / f"models--{source.replace('/', '--')}"
    snapshots_dir = model_cache / "snapshots"
    if not snapshots_dir.exists():
        return source

    snapshots = [
        path
        for path in snapshots_dir.iterdir()
        if path.is_dir() and (path / "tokenizer.json").exists()
    ]
    if not snapshots:
        return source

    latest_snapshot = max(snapshots, key=lambda path: path.stat().st_mtime)
    return str(latest_snapshot)


def load_checkpoint(path: Path, device: torch.device) -> dict[str, Any]:
    try:
        return torch.load(path, map_location=device, weights_only=False)
    except TypeError:
        return torch.load(path, map_location=device)


def resolve_max_code_lens(args: argparse.Namespace) -> list[int]:
    if not args.max_code_lens.strip():
        return [args.max_code_len]

    lengths = []
    for raw_value in args.max_code_lens.split(","):
        value = raw_value.strip()
        if not value:
            continue
        lengths.append(int(value))

    if not lengths:
        raise ValueError("--max-code-lens did not contain any lengths.")
    if any(length < 1 for length in lengths):
        raise ValueError("All max code lengths must be >= 1.")
    return lengths


def infer_model_config(
    state_dict: dict[str, torch.Tensor],
    args: argparse.Namespace,
) -> dict[str, int]:
    token_embedding = state_dict["token_embedding.weight"]
    pos_emb = state_dict["pos_emb"]
    block_indices = {
        int(match.group(1))
        for key in state_dict
        if (match := re.match(r"blocks\.(\d+)\.", key))
    }
    return {
        "vocab_size": int(token_embedding.shape[0]),
        "hidden_dim": int(args.hidden_dim or token_embedding.shape[1]),
        "num_blocks": int(args.num_blocks or (max(block_indices) + 1)),
        "max_seq_len": int(pos_emb.shape[1]),
    }


def build_model(
    state_dict: dict[str, torch.Tensor],
    tokenizer: CodeTokenizer,
    args: argparse.Namespace,
    device: torch.device,
) -> LocalConvDiffCoder:
    config = infer_model_config(state_dict, args)
    if tokenizer.vocab_size != config["vocab_size"]:
        print(
            "WARNING: tokenizer vocab size differs from checkpoint vocab size: "
            f"{tokenizer.vocab_size} != {config['vocab_size']}",
            file=sys.stderr,
        )

    model = LocalConvDiffCoder(
        vocab_size=config["vocab_size"],
        mask_token_id=tokenizer.mask_token_id,
        pad_token_id=tokenizer.pad_token_id,
        hidden_dim=config["hidden_dim"],
        num_blocks=config["num_blocks"],
        max_seq_len=config["max_seq_len"],
        dilation_factor=args.dilation_factor,
    ).to(device)
    model.load_state_dict(state_dict)
    model.eval()
    return model


def load_dataset_frame(path: Path, dataset_fraction: float, seed: int) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df[["instruction", "code"]].dropna().reset_index(drop=True)
    if not (0.0 < dataset_fraction <= 1.0):
        raise ValueError("dataset_fraction must be in (0.0, 1.0].")
    if dataset_fraction < 1.0:
        keep = max(1, int(len(df) * dataset_fraction))
        df = df.sample(n=keep, random_state=seed).reset_index(drop=True)
    return df


def validation_indices(length: int, val_split: float, seed: int) -> list[int]:
    if length < 2:
        raise ValueError("Dataset must contain at least 2 rows.")
    val_size = max(1, int(length * val_split))
    train_size = length - val_size
    if train_size < 1:
        train_size = 1
        val_size = length - 1

    generator = torch.Generator().manual_seed(seed)
    permutation = torch.randperm(length, generator=generator).tolist()
    return permutation[train_size : train_size + val_size]


def compile_generated(code: str) -> tuple[bool, str]:
    try:
        compile(code, "<generated>", "exec")
        return True, ""
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"


def parse_generated(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


def evaluate_sample(
    *,
    sample_number: int,
    dataset_index: int,
    row: pd.Series,
    model: LocalConvDiffCoder,
    tokenizer: CodeTokenizer,
    device: torch.device,
    max_prompt_len: int,
    max_code_len: int,
    steps: int,
) -> SampleResult:
    prompt_ids = tokenizer.encode_instruction(str(row["instruction"]))[:max_prompt_len]
    prompt_tensor = torch.tensor(prompt_ids, dtype=torch.long, device=device)

    start = time.perf_counter()
    with torch.no_grad():
        generated_ids = model.generate(
            prompt_tensor,
            steps=steps,
            device=str(device),
            eos_token_id=tokenizer.eos_token_id,
            max_code_len=max_code_len,
        )[0].detach().cpu().tolist()
    elapsed = time.perf_counter() - start

    generated_code = tokenizer.decode(generated_ids)
    compile_ok, compile_error = compile_generated(generated_code)
    eos_position = None
    if tokenizer.eos_token_id is not None and tokenizer.eos_token_id in generated_ids:
        eos_position = generated_ids.index(tokenizer.eos_token_id)

    return SampleResult(
        index=sample_number,
        dataset_index=dataset_index,
        instruction=str(row["instruction"]),
        target_code=str(row["code"]),
        generated_code=generated_code,
        compile_ok=compile_ok,
        compile_error=compile_error,
        parse_ok=parse_generated(generated_code),
        generated_token_count=len(generated_ids),
        generated_char_count=len(generated_code),
        target_char_count=len(str(row["code"])),
        has_mask_token_id=tokenizer.mask_token_id in generated_ids,
        has_pad_token_id=tokenizer.pad_token_id in generated_ids,
        has_eos_token_id=(
            tokenizer.eos_token_id is not None and tokenizer.eos_token_id in generated_ids
        ),
        eos_position=eos_position,
        elapsed_seconds=elapsed,
    )


def summarize(
    *,
    results: list[SampleResult],
    checkpoint: dict[str, Any],
    tokenizer: CodeTokenizer,
    args: argparse.Namespace,
    device: torch.device,
    max_code_len: int,
) -> dict[str, Any]:
    sample_count = len(results)
    compile_ok = sum(result.compile_ok for result in results)
    parse_ok = sum(result.parse_ok for result in results)
    nonempty = sum(bool(result.generated_code.strip()) for result in results)
    with_mask = sum(result.has_mask_token_id for result in results)
    with_pad = sum(result.has_pad_token_id for result in results)
    with_eos = sum(result.has_eos_token_id for result in results)
    elapsed = sum(result.elapsed_seconds for result in results)

    def mean(values: list[float]) -> float:
        return sum(values) / len(values) if values else math.nan

    return {
        "checkpoint": str(args.checkpoint),
        "device": str(device),
        "steps": args.steps,
        "max_code_len": max_code_len,
        "num_samples": sample_count,
        "compile_pass_rate": compile_ok / max(1, sample_count),
        "parse_pass_rate": parse_ok / max(1, sample_count),
        "nonempty_rate": nonempty / max(1, sample_count),
        "mask_token_id_rate": with_mask / max(1, sample_count),
        "pad_token_id_rate": with_pad / max(1, sample_count),
        "eos_token_id_rate": with_eos / max(1, sample_count),
        "avg_generated_tokens": mean([r.generated_token_count for r in results]),
        "avg_generated_chars": mean([r.generated_char_count for r in results]),
        "avg_target_chars": mean([r.target_char_count for r in results]),
        "avg_seconds_per_sample": elapsed / max(1, sample_count),
        "tokenizer_pad_token_id": tokenizer.pad_token_id,
        "tokenizer_eos_token_id": tokenizer.eos_token_id,
        "tokenizer_mask_token_id": tokenizer.mask_token_id,
        "tokenizer_pad_equals_eos": tokenizer.pad_token_id == tokenizer.eos_token_id,
        "checkpoint_epoch": checkpoint.get("epoch"),
        "checkpoint_monitor_val_loss": checkpoint.get("monitor_val_loss"),
        "checkpoint_generation_val_loss": checkpoint.get("generation_val_loss"),
        "checkpoint_denoise_monitor_val_loss": checkpoint.get("denoise_monitor_val_loss"),
        "checkpoint_best_monitor_loss": checkpoint.get("best_monitor_loss"),
    }


def write_reports(
    *,
    results: list[SampleResult],
    summary: dict[str, Any],
    args: argparse.Namespace,
    max_code_len: int,
) -> tuple[Path, Path]:
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = (
        f"{args.prefix}_{args.checkpoint.stem}_steps{args.steps}_"
        f"maxcode{max_code_len}_samples{len(results)}"
    )
    samples_path = args.output_dir / f"{stem}.jsonl"
    summary_path = args.output_dir / f"{stem}_summary.json"

    with samples_path.open("w", encoding="utf-8") as handle:
        for result in results:
            handle.write(json.dumps(asdict(result), ensure_ascii=False) + "\n")

    with summary_path.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    return samples_path, summary_path


def main() -> None:
    args = build_arg_parser().parse_args()
    if args.num_samples < 1:
        raise ValueError("num_samples must be >= 1.")
    if args.steps < 1:
        raise ValueError("steps must be >= 1.")

    if args.device == "auto":
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        device = torch.device(args.device)

    tokenizer_source = resolve_tokenizer_source(args.tokenizer)
    if tokenizer_source != args.tokenizer:
        print(f"Using cached tokenizer: {tokenizer_source}")
    tokenizer = CodeTokenizer(tokenizer_source)
    checkpoint = load_checkpoint(args.checkpoint, device)
    vocab_adaptation = adapt_state_dict_to_tokenizer(
        checkpoint["model_state_dict"],
        target_vocab_size=tokenizer.vocab_size,
        pad_token_id=tokenizer.pad_token_id,
        mask_token_id=tokenizer.mask_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    if vocab_adaptation.changed:
        print(
            "Adapted checkpoint vocab: "
            f"{vocab_adaptation.source_vocab_size} -> {vocab_adaptation.target_vocab_size}"
        )
    state_dict = vocab_adaptation.state_dict
    model = build_model(state_dict, tokenizer, args, device)

    df = load_dataset_frame(args.dataset, args.dataset_fraction, args.seed)
    val_indices = validation_indices(len(df), args.val_split, args.seed)
    selected_indices = val_indices[: min(args.num_samples, len(val_indices))]

    for max_code_len in resolve_max_code_lens(args):
        print(f"Evaluating max_code_len={max_code_len}")
        results: list[SampleResult] = []
        for sample_number, dataset_index in enumerate(selected_indices, start=1):
            row = df.iloc[dataset_index]
            result = evaluate_sample(
                sample_number=sample_number,
                dataset_index=dataset_index,
                row=row,
                model=model,
                tokenizer=tokenizer,
                device=device,
                max_prompt_len=args.max_prompt_len,
                max_code_len=max_code_len,
                steps=args.steps,
            )
            results.append(result)
            status = "OK" if result.compile_ok else "FAIL"
            print(
                f"[{sample_number}/{len(selected_indices)}] "
                f"dataset_index={dataset_index} compile={status} "
                f"tokens={result.generated_token_count} "
                f"time={result.elapsed_seconds:.2f}s"
            )

        summary = summarize(
            results=results,
            checkpoint=checkpoint,
            tokenizer=tokenizer,
            args=args,
            device=device,
            max_code_len=max_code_len,
        )
        samples_path, summary_path = write_reports(
            results=results,
            summary=summary,
            args=args,
            max_code_len=max_code_len,
        )

        print(json.dumps(summary, indent=2, ensure_ascii=False))
        print(f"Samples report: {samples_path}")
        print(f"Summary report: {summary_path}")


if __name__ == "__main__":
    main()
