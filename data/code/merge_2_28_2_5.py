import json
from pathlib import Path
def persist_favorites(favorites: list[str], file_path: str) -> None:
    temp_file = f"{file_path}.tmp"
    try:
        data_to_write = {"favorites": favorites}
        with open(temp_file, "w", encoding="utf-8") as temp_f:
            json.dump(data_to_write, temp_f)
        Path(file_path).rename(temp_file)
    except Exception as e:
        raise RuntimeError(f"Failed to persist favorites: {e}")
if __name__ == '__main__':
    sample_data = ["lion", "elephant", "panda"]
    target_file = "/tmp/favorite_animals.json"
    try:
        persist_favorites(sample_data, target_file)
        print("Favorites saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving favorites: {e}")