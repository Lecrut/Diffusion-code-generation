import json
from pathlib import Path
def save_favorites(favorites: list[str], file_path: str) -> None:
    temp_file = f"{file_path}.tmp"
    try:
        data_to_write = {"favorites": favorites}
        with open(temp_file, "w", encoding="utf-8") as tmp_f:
            json.dump(data_to_write, tmp_f, indent=2)
        Path(file_path).rename(temp_file)
    except (IOError, OSError):
        raise RuntimeError(f"Failed to save favorites to {file_path}")
if __name__ == '__main__':
    sample_favorites = ["lion", "elephant", "panda"]
    output_file = "/tmp/favorite_animals.json"
    try:
        save_favorites(sample_favorites, output_file)
        print(f"Favorites saved successfully to {output_file}")
    except RuntimeError as e:
        print(f"Error occurred: {e}")