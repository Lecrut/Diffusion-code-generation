from pathlib import Path

from datasets import Dataset, load_dataset, load_from_disk

DATASET_ID = "flytech/python-codes-25k"
DATASET_NAME = "python-codes-25k"


def _default_cache_dir(split: str) -> Path:
    repo_root = Path(__file__).resolve().parents[1]
    return repo_root / "dataset" / DATASET_NAME / split


def load_python_codes_25k(
    *,
    split: str = "train",
    cache_dir: str | Path | None = None,
    force_download: bool = False,
) -> Dataset:
    local_path = Path(cache_dir) if cache_dir is not None else _default_cache_dir(split)

    if local_path.exists() and not force_download:
        return load_from_disk(str(local_path))

    dataset = load_dataset(DATASET_ID, split=split)
    local_path.parent.mkdir(parents=True, exist_ok=True)
    dataset.save_to_disk(str(local_path))
    return dataset


def build_text_dataset(*, split: str = "train"):
    dataset = load_python_codes_25k(split=split)
    mapped = dataset.map(
        lambda example: {
            "text": f"{example['instruction']} {example['input']} {example['output']}"
        }
    )
    return mapped["text"]


if __name__ == "__main__":
    text_dataset = build_text_dataset()
    print(f"Loaded {len(text_dataset)} examples.")
    print(text_dataset[0])