import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check duplicates in dataset.csv based only on code column"
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=Path("data") / "dataset.csv",
        help="Path to dataset CSV",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data") / "reports",
        help="Directory for duplicate reports",
    )
    parser.add_argument(
        "--normalize-whitespace",
        action="store_true",
        help="Normalize code by trimming line endings and trailing spaces before duplicate check",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=50,
        help="How many largest duplicate groups to save in top report",
    )
    return parser.parse_args()


def normalize_code(text: str) -> str:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    cleaned = "\n".join(line.rstrip() for line in lines).strip()
    return cleaned


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def main() -> None:
    args = parse_args()
    dataset_path = args.dataset.resolve()
    output_dir = args.output_dir.resolve()

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    df = pd.read_csv(dataset_path, low_memory=False)
    if "code" not in df.columns:
        raise ValueError("Column 'code' not found in dataset")

    output_dir.mkdir(parents=True, exist_ok=True)

    code_series = df["code"].fillna("").astype(str)
    if args.normalize_whitespace:
        normalized_code = code_series.map(normalize_code)
    else:
        normalized_code = code_series

    code_hash = normalized_code.map(hash_text)

    work_df = pd.DataFrame(
        {
            "row_index": df.index,
            "code_hash": code_hash,
            "code_length": normalized_code.str.len(),
        }
    )

    if "id" in df.columns:
        work_df["id"] = df["id"]
    if "topic" in df.columns:
        work_df["topic"] = df["topic"]
    if "instruction" in df.columns:
        work_df["instruction"] = df["instruction"]
    if "code_file" in df.columns:
        work_df["code_file"] = df["code_file"]

    counts = work_df.groupby("code_hash", dropna=False).size().rename("count").reset_index()
    duplicate_groups = counts[counts["count"] > 1].sort_values("count", ascending=False)

    dup_rows = work_df.merge(duplicate_groups, on="code_hash", how="inner").sort_values(
        ["count", "code_hash", "row_index"], ascending=[False, True, True]
    )

    top_groups = duplicate_groups.head(args.top_n).copy()

    rows_total = len(work_df)
    duplicate_rows_total = int(dup_rows.shape[0])
    groups_total = int(duplicate_groups.shape[0])
    unique_code_total = int(counts.shape[0])

    max_group = int(duplicate_groups["count"].max()) if groups_total else 1
    mean_group = float(duplicate_groups["count"].mean()) if groups_total else 0.0

    summary = {
        "dataset": str(dataset_path),
        "rows_total": rows_total,
        "unique_code_values": unique_code_total,
        "duplicate_groups": groups_total,
        "duplicate_rows": duplicate_rows_total,
        "rows_share_duplicate": float(duplicate_rows_total / rows_total) if rows_total else 0.0,
        "largest_duplicate_group": max_group,
        "mean_duplicate_group_size": mean_group,
        "normalize_whitespace": args.normalize_whitespace,
    }

    summary_path = output_dir / "code_duplicates_summary.json"
    groups_path = output_dir / "code_duplicate_groups.csv"
    rows_path = output_dir / "code_duplicate_rows.csv"
    top_path = output_dir / "code_duplicate_top_groups.csv"

    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    duplicate_groups.to_csv(groups_path, index=False)
    dup_rows.to_csv(rows_path, index=False)
    top_groups.to_csv(top_path, index=False)

    print("Code duplicate check completed")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"Saved: {summary_path}")
    print(f"Saved: {groups_path}")
    print(f"Saved: {rows_path}")
    print(f"Saved: {top_path}")


if __name__ == "__main__":
    main()
