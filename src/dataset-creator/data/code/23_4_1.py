class ItemRegistry:
    def __init__(self):
        self._data = {}
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        self._data[name] = True
    def get_items(self) -> list[str]:
        return sorted(list(self._data.keys()))
    def remove_item(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        success = self._data.pop(name, None) is True
        return success
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_items = ["Apple", "Banana", "Cherry"]
    for item in sample_items:
        registry.add_item(item)
    print("Stored items:", registry.get_items())
    if "Banana" in registry.get_items():
        removed = registry.remove_item("Banana")
        print(f"Removed Banana? {removed}")
        final_list = registry.get_items()
        print("Final list:", final_list)