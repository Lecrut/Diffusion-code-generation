import json
from pathlib import Path
def save_favorites_to_json(favorites: list[str], file_path: str) -> None:
    temp_file = f"{file_path}.tmp"
    try:
        data = {"favorites": favorites}
        with open(temp_file, "w", encoding="utf-8") as tmp_f:
            json.dump(data, tmp_f)
        Path(file_path).rename_from(temp_file, None)
    except Exception as e:
        raise RuntimeError(f"Failed to save favorites: {e}")
if __name__ == '__main__':
    sample_data = ["lion", "elephant", "panda"]
    output_file = "/tmp/favorite_animals.json"
    try:
        save_favorites_to_json(sample_data, output_file)
        print("Favorites saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving favorites: {e}")