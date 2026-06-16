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
    def remove_item(self, name: str) -> bool:
        if name in self._data:
            del self._data[name]
            return True
        return False
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_items = ["apple", "banana", "cherry"]
    for item in sample_items:
        registry.add_item(item)
    print("Stored items:", registry.get_items())
    if not registry.remove_item("banana"):
        pass