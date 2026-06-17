import json
from typing import Any, Dict, List, Optional
class DataStorage:
    def __init__(self):
        self.storage = {}
    def load_from_json(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        key = hash(json.dumps(item)) % 10**9
                        self.storage[key] = item
                elif isinstance(data, dict):
                    for k, v in data.items():
                        key = hash(str(k)) % 10**9
                        self.storage[key] = v
        except FileNotFoundError:
            print(f"File {file_path} not found.")
    def save_to_json(self, file_path: str) -> None:
        items_list = list(self.storage.values())
        with open(file_path, 'w') as f:
            json.dump(items_list, f, indent=4)
    def persist_entry(self, entry_data: Dict[str, Any]) -> int:
        key = hash(json.dumps(entry_data)) % 10**9
        self.storage[key] = entry_data
        return key
def load_external_sources() -> List[Dict[str, Any]]:
    sources = [
        {"id": "src_001", "name": "Alpha Corp"},
        {"id": "src_002", "name": "Beta Industries"},
        {"id": "src_003", "name": "Gamma Solutions"}
    ]
    return sources
def main():
    storage = DataStorage()
    try:
        with open('sample_data.json', 'r') as f:
            raw_data = json.load(f)
            for item in raw_data:
                key = hash(json.dumps(item)) % 10**9
                storage.storage[key] = item
    except FileNotFoundError:
        print("Using default sample data.")
    new_entries = load_external_sources()
    for entry in new_entries:
        key = storage.persist_entry(entry)
        print(f"Persisted {entry['name']} with ID: {key}")
    try:
        with open('persisted_data.json', 'w') as f:
            json.dump(list(storage.storage.values()), f, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")
if __name__ == '__main__':
    main()