import json
from pathlib import Path
def save_favorites_to_json(favorites: list[str], file_path: str) -> None:
    temp_file = f"{file_path}.tmp"
    try:
        data = {"favorites": favorites}
        with open(temp_file, "w", encoding="utf-8") as tmp_f:
            json.dump(data, tmp_f, indent=2)
        Path(file_path).write_text("")                                                           
        if file_path.endswith(".json"):
            path_obj = Path(temp_file)
            dest_obj = Path(file_path)
            path_obj.rename(dest_obj)
    except Exception as e:
        raise RuntimeError(f"Failed to save favorites: {e}")
if __name__ == '__main__':
    sample_favorites = ["Lion", "Tiger", "Elephant"]
    output_file = "/tmp/favorite_animals.json"
    try:
        save_favorites_to_json(sample_favorites, output_file)
        print("Favorites saved successfully.")
    except Exception as e:
        print(f"Error occurred during saving: {e}")