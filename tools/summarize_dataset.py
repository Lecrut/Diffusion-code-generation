import argparse
import json
from collections import Counter
from pathlib import Path

import pandas as pd


BOOL_TRUE = {True, 1, "1", "true", "t", "yes", "y"}
BOOL_FALSE = {False, 0, "0", "false", "f", "no", "n"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a rich summary of dataset.csv")
    parser.add_argument(
        "--dataset",
        type=Path,
        default=Path("data") / "dataset.csv",
        help="Path to dataset CSV",
    )
    parser.add_argument(
        "--code-dir",
        type=Path,
        default=Path("data") / "code",
        help="Directory with code files referenced by code_file column",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data") / "reports",
        help="Where to write report artifacts",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=30,
        help="How many top values to keep in ranking tables",
    )
    return parser.parse_args()


def to_bool_series(series: pd.Series) -> pd.Series:
    def convert(value: object) -> object:
        if pd.isna(value):
            return pd.NA
        if isinstance(value, str):
            normalized = value.strip().lower()
        else:
            normalized = value
        if normalized in BOOL_TRUE:
            return True
        if normalized in BOOL_FALSE:
            return False
        return pd.NA

    return series.map(convert)


def numeric_summary(series: pd.Series) -> dict[str, float | int | None]:
    clean = pd.to_numeric(series, errors="coerce").dropna()
    if clean.empty:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "mean": None,
            "median": None,
            "std": None,
            "p25": None,
            "p75": None,
            "p95": None,
            "p99": None,
            "sum": None,
        }

    return {
        "count": int(clean.count()),
        "min": float(clean.min()),
        "max": float(clean.max()),
        "mean": float(clean.mean()),
        "median": float(clean.median()),
        "std": float(clean.std(ddof=0)),
        "p25": float(clean.quantile(0.25)),
        "p75": float(clean.quantile(0.75)),
        "p95": float(clean.quantile(0.95)),
        "p99": float(clean.quantile(0.99)),
        "sum": float(clean.sum()),
    }


def top_value_counts(series: pd.Series, top_n: int) -> pd.DataFrame:
    counts = series.fillna("<NA>").astype(str).value_counts().head(top_n)
    result = counts.rename_axis("value").reset_index(name="count")
    result["share"] = result["count"] / max(int(series.shape[0]), 1)
    return result


def analyze_code_files(df: pd.DataFrame, code_dir: Path, top_n: int) -> dict[str, object]:
    if "code_file" not in df.columns:
        return {"enabled": False, "reason": "Missing code_file column"}

    code_series = df["code_file"].dropna().astype(str)
    referenced = sorted({name for name in code_series if name.strip()})

    info_rows: list[dict[str, object]] = []
    missing_files: list[str] = []
    extension_counter: Counter[str] = Counter()

    for name in referenced:
        path = code_dir / name
        extension_counter[path.suffix.lower() or "<no_ext>"] += 1
        if not path.exists() or not path.is_file():
            missing_files.append(name)
            continue
        size = path.stat().st_size
        info_rows.append({"code_file": name, "size_bytes": size})

    sizes_df = pd.DataFrame(info_rows)
    size_summary = (
        numeric_summary(sizes_df["size_bytes"]) if not sizes_df.empty else numeric_summary(pd.Series(dtype=float))
    )

    return {
        "enabled": True,
        "code_dir": str(code_dir),
        "referenced_unique_files": len(referenced),
        "existing_files": len(info_rows),
        "missing_files": len(missing_files),
        "missing_files_sample": missing_files[:top_n],
        "extensions": dict(extension_counter.most_common()),
        "size_bytes": size_summary,
    }


def main() -> None:
    args = parse_args()
    dataset_path = args.dataset.resolve()
    code_dir = args.code_dir.resolve()
    output_dir = args.output_dir.resolve()

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(dataset_path, low_memory=False)

    rows, cols = df.shape
    missing_counts = df.isna().sum().sort_values(ascending=False)
    missing_pct = (missing_counts / max(rows, 1) * 100).round(4)

    if "code" in df.columns:
        code_char_len = df["code"].fillna("").astype(str).str.len()
        code_line_len = df["code"].fillna("").astype(str).str.count("\n") + 1
    else:
        code_char_len = pd.Series(dtype=float)
        code_line_len = pd.Series(dtype=float)

    boolean_metrics: dict[str, dict[str, object]] = {}
    for col in ["valid", "compile_valid", "runtime_valid"]:
        if col not in df.columns:
            continue
        normalized = to_bool_series(df[col])
        non_null = normalized.notna().sum()
        true_count = (normalized == True).sum()  # noqa: E712
        false_count = (normalized == False).sum()  # noqa: E712
        boolean_metrics[col] = {
            "non_null": int(non_null),
            "true": int(true_count),
            "false": int(false_count),
            "true_rate_on_non_null": float(true_count / non_null) if non_null else None,
            "coverage_rate": float(non_null / max(rows, 1)),
        }

    duplicate_full_rows = int(df.duplicated(keep=False).sum())
    duplicate_subset_count = (
        int(df.duplicated(subset=["topic", "instruction", "code"], keep=False).sum())
        if all(col in df.columns for col in ["topic", "instruction", "code"])
        else None
    )
    duplicate_code_count = (
        int(df.duplicated(subset=["code"], keep=False).sum()) if "code" in df.columns else None
    )
    duplicate_code_file_count = (
        int(df.duplicated(subset=["code_file"], keep=False).sum())
        if "code_file" in df.columns
        else None
    )

    top_topics = (
        top_value_counts(df["topic"], args.top_n)
        if "topic" in df.columns
        else pd.DataFrame(columns=["value", "count", "share"])
    )
    top_instructions = (
        top_value_counts(df["instruction"], args.top_n)
        if "instruction" in df.columns
        else pd.DataFrame(columns=["value", "count", "share"])
    )

    repeated_pairs = pd.DataFrame(columns=["topic", "instruction", "count"])
    if all(col in df.columns for col in ["topic", "instruction"]):
        repeated_pairs = (
            df.groupby(["topic", "instruction"], dropna=False)
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
            .head(args.top_n)
        )

    duplicate_groups = pd.DataFrame(columns=["topic", "instruction", "code", "count"])
    if all(col in df.columns for col in ["topic", "instruction", "code"]):
        duplicate_groups = (
            df.groupby(["topic", "instruction", "code"], dropna=False)
            .size()
            .reset_index(name="count")
            .query("count > 1")
            .sort_values("count", ascending=False)
            .head(args.top_n)
        )

    compile_runtime_table = pd.DataFrame()
    if all(col in df.columns for col in ["compile_valid", "runtime_valid"]):
        c = to_bool_series(df["compile_valid"]).fillna("<NA>")
        r = to_bool_series(df["runtime_valid"]).fillna("<NA>")
        compile_runtime_table = pd.crosstab(c, r, dropna=False)

    file_metrics = analyze_code_files(df, code_dir, args.top_n)

    summary = {
        "dataset_path": str(dataset_path),
        "code_dir": str(code_dir),
        "shape": {"rows": int(rows), "columns": int(cols)},
        "columns": list(df.columns),
        "unique_counts": {
            col: int(df[col].nunique(dropna=True))
            for col in [
                "topic_id",
                "instruction_id",
                "topic",
                "instruction",
                "variant_idx",
                "id",
                "code_file",
            ]
            if col in df.columns
        },
        "missing": {
            "count": {col: int(value) for col, value in missing_counts.to_dict().items()},
            "percent": {col: float(value) for col, value in missing_pct.to_dict().items()},
        },
        "code_length": {
            "characters": numeric_summary(code_char_len),
            "lines": numeric_summary(code_line_len),
        },
        "boolean_metrics": boolean_metrics,
        "duplicates": {
            "full_rows": duplicate_full_rows,
            "topic_instruction_code_rows": duplicate_subset_count,
            "code_rows": duplicate_code_count,
            "code_file_rows": duplicate_code_file_count,
        },
        "files": file_metrics,
    }

    summary_path = output_dir / "dataset_summary.json"
    missing_path = output_dir / "missing_values.csv"
    top_topics_path = output_dir / "top_topics.csv"
    top_instructions_path = output_dir / "top_instructions.csv"
    repeated_pairs_path = output_dir / "top_topic_instruction_pairs.csv"
    duplicate_groups_path = output_dir / "top_duplicate_topic_instruction_code_groups.csv"
    compile_runtime_path = output_dir / "compile_runtime_crosstab.csv"

    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    missing_df = pd.DataFrame(
        {
            "column": missing_counts.index,
            "missing_count": missing_counts.values,
            "missing_percent": [missing_pct[col] for col in missing_counts.index],
        }
    )
    missing_df.to_csv(missing_path, index=False)

    top_topics.to_csv(top_topics_path, index=False)
    top_instructions.to_csv(top_instructions_path, index=False)
    repeated_pairs.to_csv(repeated_pairs_path, index=False)
    duplicate_groups.to_csv(duplicate_groups_path, index=False)
    if not compile_runtime_table.empty:
        compile_runtime_table.to_csv(compile_runtime_path)

    print("Dataset summary created")
    print(f"Rows: {rows}")
    print(f"Columns: {cols}")
    print(f"Unique topics: {summary['unique_counts'].get('topic', 'n/a')}")
    print(f"Unique instructions: {summary['unique_counts'].get('instruction', 'n/a')}")
    print(f"Summary JSON: {summary_path}")


if __name__ == "__main__":
    main()
