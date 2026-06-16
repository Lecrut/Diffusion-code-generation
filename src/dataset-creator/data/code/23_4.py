class ItemRegistry:
    def __init__(self):
        self._items = {}
    def add(self, item_name: str) -> None:
        if not isinstance(item_name, str):
            raise TypeError("Item name must be a string.")
        self._items[item_name] = True
    def get_all_names(self) -> list[str]:
        return sorted(list(self._items.keys()))
    def remove(self, item_name: str) -> bool:
        if item_name in self._items:
            del self._items[item_name]
            return True
        return False
    def __len__(self) -> int:
        return len(self._items)
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_items = ["apple", "banana", "cherry"]
    for item in sample_items:
        registry.add(item)
    print("Stored items:", registry.get_all_names())
    assert len(registry) == 3
    removed = registry.remove("banana")
    assert removed is True
    final_list = registry.get_all_names()
    assert "banana" not in final_list and "apple" in final_list