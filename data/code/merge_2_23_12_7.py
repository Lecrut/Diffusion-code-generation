import json
from typing import Any, Dict
class ItemRegistry:
    def __init__(self):
        self._data: Dict[str, Dict[str, Any]] = {}
    def add_item(self, name: str, metadata: Dict[str, Any]) -> None:
        if not isinstance(metadata, dict):
            raise TypeError("Metadata must be a dictionary.")
        self._data[name] = metadata.copy()
    def get_item(self, name: str) -> Dict[str, Any]:
        return self._data.get(name)
    def remove_item(self, name: str) -> bool:
        removed = name in self._data
        if removed:
            del self._data[name]
        return removed
    def list_items(self) -> list[str]:
        return sorted(self._data.keys())
    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self._data, indent=indent, ensure_ascii=False)
if __name__ == '__main__':
    registry = ItemRegistry()
    items_data = {
        "apple": {"color": "red", "calories": 52, "origin": "USA"},
        "banana": {"color": "yellow", "calories": 89, "origin": "Africa"},
        "cherry": {"color": "dark red", "calories": 36, "origin": "Europe"}
    }
    for name, meta in items_data.items():
        registry.add_item(name, meta)
    print("Registered Items:")
    for item_name in registry.list_items():
        data = registry.get_item(item_name)
        if data:
            print(f"  {item_name}: {data}")
    test_remove = "banana"
    is_removed = registry.remove_item(test_remove)
    print(f"\nRemoved '{test_remove}': {is_removed}")
    remaining_data = registry.get_item("apple")
    if remaining_data:
        print(f"\nRemaining item 'apple' details: {remaining_data}")
    json_output = registry.to_json()
    print("\nJSON Representation:")
    print(json_output)