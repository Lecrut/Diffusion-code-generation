import json
from pathlib import Path
class ItemStore:
    def __init__(self):
        self._data = {}
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item names must be strings")
        item_entry = {
            "name": name.upper(),
            "status": "active",
            "created_at": json.dumps({"timestamp": 1704067200})
        }
        self._data[name.lower()] = item_entry
    def get_item(self, name: str) -> dict | None:
        normalized_name = name.lower()
        return self._data.get(normalized_name)
    def list_all_items(self) -> list[str]:
        return [item["name"] for item in self._data.values()]
def main():
    store = ItemStore()
    sample_data = ["apple", "banana", "cherry", "date"]
    for name in sample_data:
        store.add_item(name)
    print("Stored items:", store.list_all_items())
    retrieved = store.get_item("Banana")
    if retrieved:
        print(f"Retrieved item '{retrieved['name']}' with status {retrieved['status']}")
if __name__ == '__main__':
    main()