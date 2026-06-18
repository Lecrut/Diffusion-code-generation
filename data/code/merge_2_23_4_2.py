import json
class ItemRegistry:
    def __init__(self):
        self._data = {}
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        self._data[name] = True
    def get_items(self) -> list[str]:
        return sorted(list(self._data.keys()))
    def has_item(self, name: str) -> bool:
        return name in self._data
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_names = ["apple", "banana", "cherry"]
    for item in sample_names:
        registry.add_item(item)
    retrieved_items = registry.get_items()
    print("Stored items:", json.dumps(retrieved_items, indent=2))