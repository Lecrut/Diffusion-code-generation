import os
import pandas as pd


def save_dataset(records, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pd.DataFrame(records).to_csv(path, index=False)


def save_code(file_path, code_text):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(code_text)
