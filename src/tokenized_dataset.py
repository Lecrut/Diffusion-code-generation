from __future__ import annotations

import json
import gc
import random
import shutil
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset


CACHE_VERSION = 1


def _safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in value).strip("_")


def tokenized_cache_dir(
    cache_root: Path,
    tokenizer_name: str,
    max_prompt_len: int,
    max_code_len: int,
    pad_token_id: int,
    vocab_size: int,
) -> Path:
    tokenizer_part = _safe_name(tokenizer_name)
    return cache_root / (
        f"{tokenizer_part}_p{max_prompt_len}_c{max_code_len}"
        f"_pad{pad_token_id}_vocab{vocab_size}_v{CACHE_VERSION}"
    )


def _metadata_matches(metadata: dict[str, Any], expected: dict[str, Any]) -> bool:
    return all(metadata.get(key) == value for key, value in expected.items())


def _read_metadata(cache_dir: Path) -> dict[str, Any] | None:
    metadata_path = cache_dir / "metadata.json"
    if not metadata_path.is_file():
        return None
    try:
        return json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _iter_csv_chunks(csv_path: Path, chunk_size: int):
    return pd.read_csv(
        csv_path,
        usecols=["instruction", "code"],
        dtype={"instruction": "string", "code": "string"},
        chunksize=chunk_size,
        low_memory=False,
    )


def _valid_rows(chunk: pd.DataFrame) -> pd.DataFrame:
    return chunk[["instruction", "code"]].dropna()


def _count_valid_rows(csv_path: Path, chunk_size: int) -> int:
    total = 0
    for chunk in _iter_csv_chunks(csv_path, chunk_size):
        total += len(_valid_rows(chunk))
    return total


def _write_json(path: Path, payload: dict[str, Any] | list[dict[str, str]]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")


def ensure_tokenized_cache(
    *,
    csv_path: Path,
    tokenizer,
    cache_dir: Path,
    max_prompt_len: int,
    max_code_len: int,
    dataset_fraction: float = 1.0,
    chunk_size: int = 8192,
    encode_batch_size: int = 512,
    force_rebuild: bool = False,
    sample_count: int = 3,
    seed: int = 42,
) -> Path:
    if not (0.0 < dataset_fraction <= 1.0):
        raise ValueError("dataset_fraction must be in (0.0, 1.0].")

    csv_path = csv_path.resolve()
    cache_dir = cache_dir.resolve()
    stat = csv_path.stat()
    expected_metadata = {
        "cache_version": CACHE_VERSION,
        "source_csv": str(csv_path),
        "source_size": stat.st_size,
        "source_mtime_ns": stat.st_mtime_ns,
        "tokenizer_name": tokenizer.model_name,
        "vocab_size": tokenizer.vocab_size,
        "pad_token_id": tokenizer.pad_token_id,
        "max_prompt_len": max_prompt_len,
        "max_code_len": max_code_len,
        "dataset_fraction": dataset_fraction,
    }

    metadata = _read_metadata(cache_dir)
    required_files = [
        cache_dir / "prompt_ids.npy",
        cache_dir / "code_ids.npy",
        cache_dir / "prompt_lens.npy",
        cache_dir / "code_lens.npy",
        cache_dir / "samples.json",
    ]
    if (
        not force_rebuild
        and metadata is not None
        and _metadata_matches(metadata, expected_metadata)
        and all(path.is_file() for path in required_files)
    ):
        return cache_dir

    cache_dir.parent.mkdir(parents=True, exist_ok=True)
    tmp_dir = cache_dir.with_name(cache_dir.name + ".tmp")
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir(parents=True)

    print(f"[DATA] Building token cache from {csv_path}")
    count_start = time.perf_counter()
    valid_rows = _count_valid_rows(csv_path, chunk_size)
    target_rows = max(1, int(valid_rows * dataset_fraction))
    print(
        f"[DATA] Found {valid_rows:,} valid rows; caching {target_rows:,} rows "
        f"({time.perf_counter() - count_start:.1f}s count pass)."
    )

    prompt_ids = np.lib.format.open_memmap(
        tmp_dir / "prompt_ids.npy",
        mode="w+",
        dtype=np.int32,
        shape=(target_rows, max_prompt_len),
    )
    code_ids = np.lib.format.open_memmap(
        tmp_dir / "code_ids.npy",
        mode="w+",
        dtype=np.int32,
        shape=(target_rows, max_code_len),
    )
    prompt_lens = np.lib.format.open_memmap(
        tmp_dir / "prompt_lens.npy",
        mode="w+",
        dtype=np.uint16,
        shape=(target_rows,),
    )
    code_lens = np.lib.format.open_memmap(
        tmp_dir / "code_lens.npy",
        mode="w+",
        dtype=np.uint16,
        shape=(target_rows,),
    )
    prompt_ids[:] = tokenizer.pad_token_id
    code_ids[:] = tokenizer.pad_token_id
    prompt_lens[:] = 0
    code_lens[:] = 0

    written = 0
    seen = 0
    rng = random.Random(seed)
    samples: list[dict[str, str]] = []
    build_start = time.perf_counter()

    for chunk in _iter_csv_chunks(csv_path, chunk_size):
        if written >= target_rows:
            break

        rows = _valid_rows(chunk)
        if rows.empty:
            continue

        remaining = target_rows - written
        if len(rows) > remaining:
            rows = rows.iloc[:remaining]

        instructions = [str(value) for value in rows["instruction"].tolist()]
        codes = [str(value) for value in rows["code"].tolist()]

        for instruction, code in zip(instructions, codes):
            seen += 1
            sample = {"instruction": instruction, "code": code}
            if len(samples) < sample_count:
                samples.append(sample)
            else:
                slot = rng.randrange(seen)
                if slot < sample_count:
                    samples[slot] = sample

        for start in range(0, len(instructions), encode_batch_size):
            end = min(start + encode_batch_size, len(instructions))
            prompt_batch = tokenizer.batch_encode_instruction(
                instructions[start:end],
                max_length=max_prompt_len,
            )
            code_batch = tokenizer.batch_encode_code(
                codes[start:end],
                max_length=max_code_len,
            )

            for prompt, code in zip(prompt_batch, code_batch):
                prompt = prompt[:max_prompt_len]
                code = code[:max_code_len]
                prompt_len = len(prompt)
                code_len = len(code)
                prompt_lens[written] = prompt_len
                code_lens[written] = code_len
                if prompt_len:
                    prompt_ids[written, :prompt_len] = prompt
                if code_len:
                    code_ids[written, :code_len] = code
                written += 1

        if written and (written % max(chunk_size * 10, 1) == 0 or written >= target_rows):
            elapsed = max(time.perf_counter() - build_start, 1e-6)
            print(f"[DATA] Cached {written:,}/{target_rows:,} rows ({written / elapsed:.0f} rows/s).")

    prompt_ids.flush()
    code_ids.flush()
    prompt_lens.flush()
    code_lens.flush()
    del prompt_ids, code_ids, prompt_lens, code_lens
    gc.collect()

    metadata_to_write = {
        **expected_metadata,
        "rows": int(written),
        "built_at_unix": time.time(),
    }
    _write_json(tmp_dir / "metadata.json", metadata_to_write)
    _write_json(tmp_dir / "samples.json", samples)

    if written != target_rows:
        shutil.rmtree(tmp_dir)
        raise RuntimeError(f"Token cache expected {target_rows} rows but wrote {written}.")

    if cache_dir.exists():
        shutil.rmtree(cache_dir)
    tmp_dir.rename(cache_dir)
    print(f"[DATA] Token cache ready: {cache_dir}")
    return cache_dir


class TokenizedMemmapDataset(Dataset):
    def __init__(self, cache_dir: Path, indices: np.ndarray | None = None):
        self.cache_dir = Path(cache_dir)
        self.prompt_ids = np.load(self.cache_dir / "prompt_ids.npy", mmap_mode="r")
        self.code_ids = np.load(self.cache_dir / "code_ids.npy", mmap_mode="r")
        self.prompt_lens = np.load(self.cache_dir / "prompt_lens.npy", mmap_mode="r")
        self.code_lens = np.load(self.cache_dir / "code_lens.npy", mmap_mode="r")
        self.indices = None if indices is None else np.asarray(indices, dtype=np.int64)

        if self.prompt_ids.shape[0] != self.code_ids.shape[0]:
            raise ValueError("prompt_ids and code_ids cache files have different row counts.")

    def __len__(self) -> int:
        if self.indices is not None:
            return int(self.indices.shape[0])
        return int(self.prompt_ids.shape[0])

    def __getitem__(self, idx: int) -> dict[str, np.ndarray]:
        row_idx = int(self.indices[idx]) if self.indices is not None else int(idx)
        return {
            "prompt_ids": self.prompt_ids[row_idx],
            "code_ids": self.code_ids[row_idx],
        }


def make_train_val_indices(
    total_rows: int,
    *,
    val_split: float,
    max_val_samples: int,
    seed: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    if not (0.0 < val_split < 1.0):
        raise ValueError("val_split must be in (0.0, 1.0).")

    val_size = max(1, int(total_rows * val_split))
    if max_val_samples > 0:
        val_size = min(val_size, max_val_samples)

    rng = np.random.default_rng(seed)
    val_indices = np.sort(rng.choice(total_rows, size=val_size, replace=False))
    train_mask = np.ones(total_rows, dtype=bool)
    train_mask[val_indices] = False
    train_indices = np.flatnonzero(train_mask)
    return train_indices.astype(np.int64), val_indices.astype(np.int64)


def collate_tokenized_batch(batch: list[dict[str, np.ndarray]]) -> dict[str, torch.Tensor]:
    prompt_ids = np.stack([item["prompt_ids"] for item in batch], axis=0).astype(np.int64, copy=False)
    code_ids = np.stack([item["code_ids"] for item in batch], axis=0).astype(np.int64, copy=False)
    return {
        "prompt_ids": torch.from_numpy(prompt_ids),
        "code_ids": torch.from_numpy(code_ids),
    }


def load_cached_samples(cache_dir: Path) -> list[dict[str, str]]:
    samples_path = Path(cache_dir) / "samples.json"
    if not samples_path.is_file():
        return []
    try:
        samples = json.loads(samples_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    return [
        {"instruction": str(item.get("instruction", "")), "code": str(item.get("code", ""))}
        for item in samples
        if isinstance(item, dict)
    ]
