import json
from pathlib import Path
class EfficientTextStore:
    def __init__(self):
        self._data = {}
    def add(self, key: str, value: str) -> None:
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Key and value must be strings")
        self._data[key] = value
    def get(self, key: str) -> str | None:
        return self._data.get(key)
    def delete(self, key: str) -> bool:
        if key in self._data:
            del self._data[key]
            return True
        return False
    def clear(self) -> None:
        self._data.clear()
def serialize(data):
    with open("storage.json", "w") as f:
        json.dump(data, f)
def deserialize():
    path = Path("storage.json")
    if not path.exists():
        return {}
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
if __name__ == '__main__':
    store = EfficientTextStore()
    sample_data = {
        "user_001": "Alice",
        "item_id_A": "Widget X",
        "session_xyz": "Token 998"
    }
    for k, v in sample_data.items():
        store.add(k, v)
    serialize(store._data)
    print("Stored items:")
    for key in sorted(sample_data.keys()):
        val = store.get(key)
        if val:
            print(f"{key}: {val}")