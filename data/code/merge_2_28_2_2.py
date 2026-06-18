import json
from pathlib import Path
def persist_favorites(favorites: list[str], filename: str = "favorites.json") -> None:
    temp_filename = f"{filename}.tmp"
    try:
        data_to_write = {"animals": favorites}
        with open(temp_filename, 'w', encoding='utf-8') as temp_file:
            json.dump(data_to_write, temp_file, indent=2)
        Path(filename).write_text(Path(temp_filename).read_text())
    except Exception as e:
        raise RuntimeError(f"Failed to persist favorites due to {e}")
if __name__ == '__main__':
    sample_favorites = ["Lion", "Tiger", "Elephant"]
    persist_favorites(sample_favorites)