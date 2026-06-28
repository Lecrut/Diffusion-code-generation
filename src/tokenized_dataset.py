from __future__ import annotations

import json
import gc
import hashlib
import random
import re
import shutil
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset


CACHE_VERSION = 4
COMPILE_FILTER_MODES = {"none", "exclude_false", "require_true"}


def _safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in value).strip("_")


def tokenized_cache_dir(
    cache_root: Path,
    tokenizer_name: str,
    max_prompt_len: int,
    max_code_len: int,
    pad_token_id: int,
    vocab_size: int,
    dataset_fraction: float = 1.0,
    max_ast_len: int = 256,
    require_valid: bool = False,
    compile_filter: str = "none",
    canonicalize_instructions: bool = False,
) -> Path:
    tokenizer_part = _safe_name(tokenizer_name)
    frac_suffix = f"_frac{dataset_fraction}" if dataset_fraction != 1.0 else ""
    ast_part = f"_ast{max_ast_len}"
    req_part = f"_req{int(require_valid)}"
    cf_part = f"_cf_{compile_filter}"
    canon_part = f"_canon{int(canonicalize_instructions)}"
    return cache_root / (
        f"{tokenizer_part}_p{max_prompt_len}_c{max_code_len}"
        f"_pad{pad_token_id}_vocab{vocab_size}_v{CACHE_VERSION}{frac_suffix}"
        f"{ast_part}{req_part}{cf_part}{canon_part}"
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


def _read_csv_columns(csv_path: Path) -> list[str]:
    return list(pd.read_csv(csv_path, nrows=0).columns)


def _csv_use_columns(csv_path: Path) -> list[str]:
    columns = _read_csv_columns(csv_path)
    required = {"instruction", "code"}
    missing = sorted(required - set(columns))
    if missing:
        raise ValueError(f"{csv_path} is missing required column(s): {missing}")
    optional = [column for column in ("valid", "compile_valid") if column in columns]
    return ["instruction", "code", *optional]


def _iter_csv_chunks(csv_path: Path, chunk_size: int, usecols: list[str] | None = None):
    return pd.read_csv(
        csv_path,
        usecols=usecols or _csv_use_columns(csv_path),
        dtype={"instruction": "string", "code": "string"},
        chunksize=chunk_size,
        low_memory=False,
    )


def _bool_masks(series: pd.Series) -> tuple[pd.Series, pd.Series]:
    normalized = series.astype("string").str.strip().str.lower()
    true_mask = series.eq(True) | normalized.isin({"1", "true", "yes", "y"})
    false_mask = series.eq(False) | normalized.isin({"0", "false", "no", "n"})
    return true_mask.fillna(False), false_mask.fillna(False)


def _instruction_key(value: str) -> str:
    return re.sub(r"\s+", " ", str(value).lower().strip())


def _code_key(value: str) -> bytes:
    return hashlib.blake2b(str(value).encode("utf-8", errors="replace"), digest_size=16).digest()


def _valid_rows(
    chunk: pd.DataFrame,
    *,
    require_valid: bool = False,
    compile_filter: str = "none",
    canonicalize_instructions: bool = False,
    seen_instruction_keys: set[str] | None = None,
) -> pd.DataFrame:
    if compile_filter not in COMPILE_FILTER_MODES:
        raise ValueError(f"compile_filter must be one of {sorted(COMPILE_FILTER_MODES)}, got {compile_filter!r}.")

    rows = chunk.dropna(subset=["instruction", "code"])

    if require_valid and "valid" in rows.columns:
        valid_true, _ = _bool_masks(rows["valid"])
        rows = rows[valid_true]

    if compile_filter != "none" and "compile_valid" in rows.columns:
        compile_true, compile_false = _bool_masks(rows["compile_valid"])
        if compile_filter == "require_true":
            rows = rows[compile_true]
        elif compile_filter == "exclude_false":
            rows = rows[~compile_false]

    if canonicalize_instructions:
        if seen_instruction_keys is None:
            raise ValueError("seen_instruction_keys is required when canonicalize_instructions=True.")
        keep_indices = []
        for idx, instruction in rows["instruction"].items():
            key = _instruction_key(str(instruction))
            if key in seen_instruction_keys:
                continue
            seen_instruction_keys.add(key)
            keep_indices.append(idx)
        rows = rows.loc[keep_indices]

    return rows[["instruction", "code"]]


def _scan_reference_groups(
    csv_path: Path,
    chunk_size: int,
    *,
    usecols: list[str],
    require_valid: bool,
    compile_filter: str,
) -> tuple[dict[str, int], list[str], np.ndarray, int]:
    group_key_to_id: dict[str, int] = {}
    group_keys: list[str] = []
    group_ref_counts: list[int] = []
    seen_code_keys: list[set[bytes]] = []
    reference_rows = 0

    reader = _iter_csv_chunks(csv_path, chunk_size, usecols)
    try:
        for chunk in reader:
            rows = _valid_rows(
                chunk,
                require_valid=require_valid,
                compile_filter=compile_filter,
                canonicalize_instructions=False,
            )
            for instruction, code in zip(rows["instruction"], rows["code"]):
                instruction_key = _instruction_key(str(instruction))
                group_id = group_key_to_id.get(instruction_key)
                if group_id is None:
                    group_id = len(group_keys)
                    group_key_to_id[instruction_key] = group_id
                    group_keys.append(instruction_key)
                    group_ref_counts.append(0)
                    seen_code_keys.append(set())

                code_key = _code_key(str(code))
                if code_key in seen_code_keys[group_id]:
                    continue
                seen_code_keys[group_id].add(code_key)
                group_ref_counts[group_id] += 1
                reference_rows += 1
    finally:
        close = getattr(reader, "close", None)
        if close is not None:
            close()

    return (
        group_key_to_id,
        group_keys,
        np.asarray(group_ref_counts, dtype=np.int64),
        reference_rows,
    )


def _count_valid_rows(
    csv_path: Path,
    chunk_size: int,
    *,
    usecols: list[str],
    require_valid: bool,
    compile_filter: str,
    canonicalize_instructions: bool,
) -> int:
    total = 0
    seen_instruction_keys: set[str] | None = set() if canonicalize_instructions else None
    reader = _iter_csv_chunks(csv_path, chunk_size, usecols)
    try:
        for chunk in reader:
            total += len(
                _valid_rows(
                    chunk,
                    require_valid=require_valid,
                    compile_filter=compile_filter,
                    canonicalize_instructions=canonicalize_instructions,
                    seen_instruction_keys=seen_instruction_keys,
                )
            )
    finally:
        close = getattr(reader, "close", None)
        if close is not None:
            close()
    return total


def _write_json(path: Path, payload: dict[str, Any] | list[dict[str, Any]]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")


def _collect_samples(
    csv_path: Path,
    chunk_size: int,
    *,
    usecols: list[str],
    require_valid: bool,
    compile_filter: str,
    canonicalize_instructions: bool,
    sample_count: int,
    seed: int,
    max_rows: int | None = None,
) -> list[dict[str, str]]:
    if sample_count <= 0:
        return []

    rng = random.Random(seed)
    samples: list[dict[str, str]] = []
    seen = 0
    seen_instruction_keys: set[str] | None = set() if canonicalize_instructions else None

    reader = _iter_csv_chunks(csv_path, chunk_size, usecols)
    try:
        for chunk in reader:
            rows = _valid_rows(
                chunk,
                require_valid=require_valid,
                compile_filter=compile_filter,
                canonicalize_instructions=canonicalize_instructions,
                seen_instruction_keys=seen_instruction_keys,
            )
            for instruction, code in zip(rows["instruction"], rows["code"]):
                seen += 1
                sample = {"instruction": str(instruction), "code": str(code)}
                if len(samples) < sample_count:
                    samples.append(sample)
                else:
                    slot = rng.randrange(seen)
                    if slot < sample_count:
                        samples[slot] = sample
                if max_rows is not None and seen >= max_rows:
                    return samples
    finally:
        close = getattr(reader, "close", None)
        if close is not None:
            close()

    return samples


def _ensure_cached_samples(
    cache_dir: Path,
    csv_path: Path,
    chunk_size: int,
    *,
    usecols: list[str],
    require_valid: bool,
    compile_filter: str,
    canonicalize_instructions: bool,
    sample_count: int,
    seed: int,
) -> None:
    samples_path = cache_dir / "samples.json"
    try:
        existing = json.loads(samples_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        existing = []
    if isinstance(existing, list) and len(existing) >= sample_count:
        return
    metadata = _read_metadata(cache_dir) or {}
    max_rows = metadata.get("rows")
    max_rows = None if max_rows is None else int(max_rows)

    samples = _collect_samples(
        csv_path,
        chunk_size,
        usecols=usecols,
        require_valid=require_valid,
        compile_filter=compile_filter,
        canonicalize_instructions=canonicalize_instructions,
        sample_count=sample_count,
        seed=seed,
        max_rows=max_rows,
    )
    _write_json(samples_path, samples)


import ast

AST_NODE_TYPES = [
    "PAD", "UNK",
    "Module", "FunctionDef", "AsyncFunctionDef", "ClassDef", "Return", "Delete",
    "Assign", "AugAssign", "AnnAssign", "For", "AsyncFor", "While", "If", "With",
    "AsyncWith", "Raise", "Try", "Assert", "Import", "ImportFrom", "Global",
    "Nonlocal", "Expr", "Pass", "Break", "Continue", "Constant", "Attribute",
    "Subscript", "Starred", "Name", "List", "Tuple", "Slice", "BinOp", "UnaryOp",
    "Lambda", "IfExp", "Dict", "Set", "ListComp", "SetComp", "DictComp",
    "GeneratorExp", "Await", "Yield", "YieldFrom", "Compare", "Call",
    "FormattedValue", "JoinedStr", "NameConstant", "Ellipsis", "Num", "Str",
    "Bytes", "Index", "ExtSlice", "Load", "Store", "Del", "And", "Or", "Add",
    "Sub", "Mult", "MatMult", "Div", "Mod", "Pow", "LShift", "RShift", "BitOr",
    "BitXor", "BitAnd", "FloorDiv", "Invert", "Not", "UAdd", "USub", "Eq",
    "NotEq", "Lt", "LtE", "Gt", "GtE", "Is", "IsNot", "In", "NotIn",
    "ExceptHandler", "arg", "arguments", "keyword", "withitem", "alias",
    "comprehension", "match_case", "Match", "MatchValue", "MatchSingleton",
    "MatchSequence", "MatchMapping", "MatchClass", "MatchAs", "MatchOr"
]

def code_to_ast_node_ids(code_text: str, vocab: dict[str, int], max_ast_len: int) -> tuple[list[int], int]:
    try:
        tree = ast.parse(code_text)
    except Exception:
        return [vocab["UNK"]] + [vocab["PAD"]] * (max_ast_len - 1), 1
    
    node_ids = []
    def traverse(node):
        if len(node_ids) >= max_ast_len:
            return
        node_name = node.__class__.__name__
        if node_name not in vocab:
            vocab[node_name] = len(vocab)
        node_ids.append(vocab[node_name])
        for child in ast.iter_child_nodes(node):
            traverse(child)
            if len(node_ids) >= max_ast_len:
                return

    traverse(tree)
    actual_len = len(node_ids)
    if len(node_ids) < max_ast_len:
        node_ids.extend([vocab["PAD"]] * (max_ast_len - len(node_ids)))
    return node_ids, actual_len

def ensure_tokenized_cache(
    *,
    csv_path: Path,
    tokenizer,
    cache_dir: Path,
    max_prompt_len: int,
    max_code_len: int,
    max_ast_len: int = 256,
    dataset_fraction: float = 1.0,
    chunk_size: int = 8192,
    encode_batch_size: int = 512,
    force_rebuild: bool = False,
    sample_count: int = 3,
    seed: int = 42,
    require_valid: bool = False,
    compile_filter: str = "none",
    canonicalize_instructions: bool = False,
) -> Path:
    if not (0.0 < dataset_fraction <= 1.0):
        raise ValueError("dataset_fraction must be in (0.0, 1.0].")
    if compile_filter not in COMPILE_FILTER_MODES:
        raise ValueError(f"compile_filter must be one of {sorted(COMPILE_FILTER_MODES)}, got {compile_filter!r}.")

    csv_path = csv_path.resolve()
    cache_dir = cache_dir.resolve()
    stat = csv_path.stat()
    usecols = _csv_use_columns(csv_path)
    group_key_to_id, group_keys, group_ref_counts, reference_rows = _scan_reference_groups(
        csv_path,
        chunk_size,
        usecols=usecols,
        require_valid=require_valid,
        compile_filter=compile_filter,
    )
    expected_metadata = {
        "cache_version": CACHE_VERSION,
        "source_csv": str(csv_path),
        "source_size": stat.st_size,
        "source_mtime_ns": stat.st_mtime_ns,
        "tokenizer_name": tokenizer.model_name,
        "vocab_size": tokenizer.vocab_size,
        "pad_token_id": tokenizer.pad_token_id,
        "code_eos_token_id": tokenizer.code_eos_token_id,
        "max_prompt_len": max_prompt_len,
        "max_code_len": max_code_len,
        "max_ast_len": max_ast_len,
        "dataset_fraction": dataset_fraction,
        "require_valid": bool(require_valid),
        "compile_filter": compile_filter,
        "canonicalize_instructions": bool(canonicalize_instructions),
        "reference_rows": int(reference_rows),
        "reference_groups": int(len(group_keys)),
    }

    metadata = _read_metadata(cache_dir)
    required_files = [
        cache_dir / "prompt_ids.npy",
        cache_dir / "code_ids.npy",
        cache_dir / "prompt_lens.npy",
        cache_dir / "code_lens.npy",
        cache_dir / "group_ids.npy",
        cache_dir / "ast_node_ids.npy",
        cache_dir / "ast_lengths.npy",
        cache_dir / "ast_vocab.json",
        cache_dir / "reference_code_ids.npy",
        cache_dir / "reference_code_lens.npy",
        cache_dir / "group_ref_offsets.npy",
        cache_dir / "samples.json",
        cache_dir / "group_keys.json",
    ]
    if (
        not force_rebuild
        and metadata is not None
        and _metadata_matches(metadata, expected_metadata)
        and all(path.is_file() for path in required_files)
    ):
        _ensure_cached_samples(
            cache_dir,
            csv_path,
            chunk_size,
            usecols=usecols,
            require_valid=require_valid,
            compile_filter=compile_filter,
            canonicalize_instructions=canonicalize_instructions,
            sample_count=sample_count,
            seed=seed,
        )
        return cache_dir

    cache_dir.parent.mkdir(parents=True, exist_ok=True)
    tmp_dir = cache_dir.with_name(cache_dir.name + ".tmp")
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir(parents=True)

    print(f"[DATA] Building token cache from {csv_path}")
    count_start = time.perf_counter()
    valid_rows = _count_valid_rows(
        csv_path,
        chunk_size,
        usecols=usecols,
        require_valid=require_valid,
        compile_filter=compile_filter,
        canonicalize_instructions=canonicalize_instructions,
    )
    if valid_rows <= 0:
        raise RuntimeError(
            "No dataset rows remain after filtering. "
            f"require_valid={require_valid}, compile_filter={compile_filter!r}, "
            f"canonicalize_instructions={canonicalize_instructions}."
        )
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
    group_ids = np.lib.format.open_memmap(
        tmp_dir / "group_ids.npy",
        mode="w+",
        dtype=np.int32,
        shape=(target_rows,),
    )
    ast_node_ids = np.lib.format.open_memmap(
        tmp_dir / "ast_node_ids.npy",
        mode="w+",
        dtype=np.int32,
        shape=(target_rows, max_ast_len),
    )
    ast_lengths = np.lib.format.open_memmap(
        tmp_dir / "ast_lengths.npy",
        mode="w+",
        dtype=np.uint16,
        shape=(target_rows,),
    )
    reference_code_ids = np.lib.format.open_memmap(
        tmp_dir / "reference_code_ids.npy",
        mode="w+",
        dtype=np.int32,
        shape=(reference_rows, max_code_len),
    )
    reference_code_lens = np.lib.format.open_memmap(
        tmp_dir / "reference_code_lens.npy",
        mode="w+",
        dtype=np.uint16,
        shape=(reference_rows,),
    )
    group_ref_offsets = np.zeros(len(group_ref_counts) + 1, dtype=np.int64)
    if group_ref_counts.size:
        group_ref_offsets[1:] = np.cumsum(group_ref_counts)
    np.save(tmp_dir / "group_ref_offsets.npy", group_ref_offsets)
    prompt_ids[:] = tokenizer.pad_token_id
    code_ids[:] = tokenizer.pad_token_id
    prompt_lens[:] = 0
    code_lens[:] = 0
    group_ids[:] = -1
    ast_node_ids[:] = 0  # 0 is PAD ID
    ast_lengths[:] = 0
    reference_code_ids[:] = tokenizer.pad_token_id
    reference_code_lens[:] = 0

    ast_vocab = {name: idx for idx, name in enumerate(AST_NODE_TYPES)}

    ref_write_positions = group_ref_offsets[:-1].copy()
    ref_seen_code_keys: list[set[bytes]] = [set() for _ in group_keys]
    ref_reader = _iter_csv_chunks(csv_path, chunk_size, usecols)
    try:
        for chunk in ref_reader:
            rows = _valid_rows(
                chunk,
                require_valid=require_valid,
                compile_filter=compile_filter,
                canonicalize_instructions=False,
            )
            if rows.empty:
                continue

            unique_codes: list[str] = []
            unique_group_ids: list[int] = []
            for instruction, code in zip(rows["instruction"], rows["code"]):
                instruction_key = _instruction_key(str(instruction))
                group_id = group_key_to_id[instruction_key]
                code_text = str(code)
                code_key = _code_key(code_text)
                if code_key in ref_seen_code_keys[group_id]:
                    continue
                ref_seen_code_keys[group_id].add(code_key)
                unique_codes.append(code_text)
                unique_group_ids.append(group_id)

            for start in range(0, len(unique_codes), encode_batch_size):
                end = min(start + encode_batch_size, len(unique_codes))
                code_batch = tokenizer.batch_encode_code(
                    unique_codes[start:end],
                    max_length=max_code_len,
                )
                for code, group_id in zip(code_batch, unique_group_ids[start:end]):
                    code = code[:max_code_len]
                    ref_idx = int(ref_write_positions[group_id])
                    reference_code_lens[ref_idx] = len(code)
                    if code:
                        reference_code_ids[ref_idx, : len(code)] = code
                    ref_write_positions[group_id] += 1
    finally:
        close = getattr(ref_reader, "close", None)
        if close is not None:
            close()

    reference_code_ids.flush()
    reference_code_lens.flush()

    written = 0
    seen = 0
    rng = random.Random(seed)
    samples: list[dict[str, str]] = []
    build_start = time.perf_counter()
    seen_instruction_keys: set[str] | None = set() if canonicalize_instructions else None

    reader = _iter_csv_chunks(csv_path, chunk_size, usecols)
    try:
        for chunk in reader:
            if written >= target_rows:
                break

            rows = _valid_rows(
                chunk,
                require_valid=require_valid,
                compile_filter=compile_filter,
                canonicalize_instructions=canonicalize_instructions,
                seen_instruction_keys=seen_instruction_keys,
            )
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

                for local_idx, (prompt, code) in enumerate(zip(prompt_batch, code_batch)):
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
                    instruction_key = _instruction_key(instructions[start + local_idx])
                    group_ids[written] = group_key_to_id[instruction_key]

                    # Parse AST sequence
                    raw_code = codes[start + local_idx]
                    ast_ids, ast_len = code_to_ast_node_ids(raw_code, ast_vocab, max_ast_len)
                    ast_node_ids[written, :] = ast_ids
                    ast_lengths[written] = ast_len

                    written += 1

            if written and (written % max(chunk_size * 10, 1) == 0 or written >= target_rows):
                elapsed = max(time.perf_counter() - build_start, 1e-6)
                print(f"[DATA] Cached {written:,}/{target_rows:,} rows ({written / elapsed:.0f} rows/s).")
    finally:
        close = getattr(reader, "close", None)
        if close is not None:
            close()

    prompt_ids.flush()
    code_ids.flush()
    prompt_lens.flush()
    code_lens.flush()
    group_ids.flush()
    ast_node_ids.flush()
    ast_lengths.flush()
    del prompt_ids, code_ids, prompt_lens, code_lens, group_ids, ast_node_ids, ast_lengths
    del reference_code_ids, reference_code_lens
    gc.collect()

    metadata_to_write = {
        **expected_metadata,
        "rows": int(written),
        "sample_count": int(sample_count),
        "built_at_unix": time.time(),
    }
    _write_json(tmp_dir / "metadata.json", metadata_to_write)
    _write_json(tmp_dir / "samples.json", samples)
    _write_json(tmp_dir / "group_keys.json", [{"group_id": idx, "instruction_key": key} for idx, key in enumerate(group_keys)])
    _write_json(tmp_dir / "ast_vocab.json", ast_vocab)

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
        self.indices = None if indices is None else np.asarray(indices, dtype=np.int64)
        self._open_memmaps()
        self._validate_cache()

    def _open_memmaps(self) -> None:
        self.prompt_ids = np.load(self.cache_dir / "prompt_ids.npy", mmap_mode="r")
        self.code_ids = np.load(self.cache_dir / "code_ids.npy", mmap_mode="r")
        self.prompt_lens = np.load(self.cache_dir / "prompt_lens.npy", mmap_mode="r")
        self.code_lens = np.load(self.cache_dir / "code_lens.npy", mmap_mode="r")
        self.group_ids = np.load(self.cache_dir / "group_ids.npy", mmap_mode="r")
        self.ast_node_ids = None
        self.ast_lengths = None
        if (self.cache_dir / "ast_node_ids.npy").is_file():
            self.ast_node_ids = np.load(self.cache_dir / "ast_node_ids.npy", mmap_mode="r")
            self.ast_lengths = np.load(self.cache_dir / "ast_lengths.npy", mmap_mode="r")

    def _validate_cache(self) -> None:
        if self.prompt_ids.shape[0] != self.code_ids.shape[0]:
            raise ValueError("prompt_ids and code_ids cache files have different row counts.")
        if self.prompt_lens.shape[0] != self.prompt_ids.shape[0]:
            raise ValueError("prompt_lens and prompt_ids cache files have different row counts.")
        if self.code_lens.shape[0] != self.code_ids.shape[0]:
            raise ValueError("code_lens and code_ids cache files have different row counts.")
        if self.group_ids.shape[0] != self.code_ids.shape[0]:
            raise ValueError("group_ids and code_ids cache files have different row counts.")
        if self.ast_node_ids is not None:
            if self.ast_node_ids.shape[0] != self.code_ids.shape[0]:
                raise ValueError("ast_node_ids and code_ids cache files have different row counts.")
            if self.ast_lengths.shape[0] != self.code_ids.shape[0]:
                raise ValueError("ast_lengths and code_ids cache files have different row counts.")

    def __getstate__(self) -> dict[str, Any]:
        state = self.__dict__.copy()
        state["prompt_ids"] = None
        state["code_ids"] = None
        state["prompt_lens"] = None
        state["code_lens"] = None
        state["group_ids"] = None
        state["ast_node_ids"] = None
        state["ast_lengths"] = None
        return state

    def __setstate__(self, state: dict[str, Any]) -> None:
        self.__dict__.update(state)
        self._open_memmaps()
        self._validate_cache()

    def __len__(self) -> int:
        if self.indices is not None:
            return int(self.indices.shape[0])
        return int(self.prompt_ids.shape[0])

    def __getitem__(self, idx: int) -> dict[str, np.ndarray]:
        row_idx = int(self.indices[idx]) if self.indices is not None else int(idx)
        res = {
            "prompt_ids": self.prompt_ids[row_idx],
            "code_ids": self.code_ids[row_idx],
            "code_len": np.array(self.code_lens[row_idx], dtype=np.int64),
            "group_id": np.array(self.group_ids[row_idx], dtype=np.int64),
            "sample_id": np.array(row_idx, dtype=np.int64),
        }
        if self.ast_node_ids is not None:
            res["ast_node_ids"] = self.ast_node_ids[row_idx]
            res["ast_length"] = np.array(self.ast_lengths[row_idx], dtype=np.int64)
        return res


def make_train_val_indices(
    total_rows: int,
    *,
    val_split: float,
    max_val_samples: int,
    seed: int = 42,
    group_ids: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    if not (0.0 < val_split < 1.0):
        raise ValueError("val_split must be in (0.0, 1.0).")

    if group_ids is None or len(group_ids) == 0:
        val_size = max(1, int(total_rows * val_split))
        if max_val_samples > 0:
            val_size = min(val_size, max_val_samples)

        rng = np.random.default_rng(seed)
        val_indices = np.sort(rng.choice(total_rows, size=val_size, replace=False))
        train_mask = np.ones(total_rows, dtype=bool)
        train_mask[val_indices] = False
        train_indices = np.flatnonzero(train_mask)
        return train_indices.astype(np.int64), val_indices.astype(np.int64)

    # Group-based split to avoid train-val leakage (Cause 7)
    unique_groups = np.unique(group_ids)
    rng = np.random.default_rng(seed)
    shuffled_groups = rng.permutation(unique_groups)

    # Count samples in each group for accurate target split estimation
    group_counts = {}
    for g in group_ids:
        g_val = int(g)
        group_counts[g_val] = group_counts.get(g_val, 0) + 1

    val_indices_list = []
    train_indices_list = []
    current_val_size = 0
    target_val_size = int(total_rows * val_split)
    if max_val_samples > 0:
        target_val_size = min(target_val_size, max_val_samples)

    val_groups = set()
    for g in shuffled_groups:
        g_val = int(g)
        count = group_counts[g_val]
        if current_val_size + count <= target_val_size or not val_groups:
            val_groups.add(g_val)
            current_val_size += count

    for idx, g in enumerate(group_ids):
        g_val = int(g)
        if g_val in val_groups:
            val_indices_list.append(idx)
        else:
            train_indices_list.append(idx)

    val_indices = np.array(val_indices_list, dtype=np.int64)
    train_indices = np.array(train_indices_list, dtype=np.int64)

    return train_indices, val_indices


def collate_tokenized_batch(batch: list[dict[str, np.ndarray]]) -> dict[str, torch.Tensor]:
    prompt_ids = np.stack([item["prompt_ids"] for item in batch], axis=0).astype(np.int64, copy=False)
    code_ids = np.stack([item["code_ids"] for item in batch], axis=0).astype(np.int64, copy=False)
    sample_ids = np.stack([item["sample_id"] for item in batch], axis=0).astype(np.int64, copy=False)
    code_lens = np.stack([item["code_len"] for item in batch], axis=0).astype(np.int64, copy=False)
    group_ids = np.stack([item["group_id"] for item in batch], axis=0).astype(np.int64, copy=False)
    res = {
        "prompt_ids": torch.from_numpy(prompt_ids),
        "code_ids": torch.from_numpy(code_ids),
        "code_len": torch.from_numpy(code_lens),
        "group_id": torch.from_numpy(group_ids),
        "sample_id": torch.from_numpy(sample_ids),
    }
    if "ast_node_ids" in batch[0]:
        ast_node_ids = np.stack([item["ast_node_ids"] for item in batch], axis=0).astype(np.int64, copy=False)
        ast_lengths = np.stack([item["ast_length"] for item in batch], axis=0).astype(np.int64, copy=False)
        res["ast_node_ids"] = torch.from_numpy(ast_node_ids)
        res["ast_length"] = torch.from_numpy(ast_lengths)
        
        # Build ast_mask: [batch_size, max_ast_len]
        max_ast_len = ast_node_ids.shape[1]
        arange = torch.arange(max_ast_len).unsqueeze(0)  # [1, max_ast_len]
        ast_mask = arange < res["ast_length"].unsqueeze(1)  # [batch_size, max_ast_len]
        res["ast_mask"] = ast_mask
        
    return res


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
