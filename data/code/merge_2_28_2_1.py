import json
import os
def save_favorites_to_json(favorites: list[str], file_path: str) -> None:
    temp_file = f"{file_path}.tmp"
    try:
        with open(temp_file, "w", encoding="utf-8") as temp_f:
            json.dump(favorites, temp_f, indent=2)
        os.replace(temp_file, file_path)
    except FileNotFoundError:
        raise RuntimeError("Target JSON directory does not exist.")
    except PermissionError:
        raise RuntimeError("Insufficient permissions to write to the target path.")
if __name__ == '__main__':
    sample_favorites = ["Lion", "Elephant", "Tiger"]
    file_path = "./favorites.json"
    save_favorites_to_json(sample_favorites, file_path)