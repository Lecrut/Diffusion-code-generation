class ItemRegistry:
    def __init__(self):
        self._items = {}
    def add(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        self._items[name] = True
    def get_all_names(self) -> list[str]:
        return sorted(list(self._items.keys()))
    def remove(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        return self._items.pop(name, None) is not None
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_items = ["apple", "banana", "cherry"]
    for item in sample_items:
        registry.add(item)
    print("Stored items:", registry.get_all_names())
    removed_item = "banana"
    if registry.remove(removed_item):
        print(f"{removed_item} was successfully removed.")
    final_list = registry.get_all_names()
    print("Remaining items:", final_list)