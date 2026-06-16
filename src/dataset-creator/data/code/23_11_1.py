class ItemManager:
    def __init__(self) -> None:
        self._items: dict[str, str] = {}
    def add_item(self, name: str, value: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(value, str):
            raise TypeError("Item value must be a string.")
        self._items[name] = value
        return True
    def get_item(self, name: str) -> str | None:
        if not isinstance(name, str):
            raise TypeError("Search key must be a string.")
        return self._items.get(name)
    def update_item(self, name: str, new_value: str) -> bool:
        current = self.get_item(name)
        if current is None:
            print(f"Item '{name}' not found. Cannot update.")
            return False
        try:
            self._items[name] = new_value
            return True
        except Exception as e:
            raise RuntimeError(f"Failed to update item {e}")
    def list_items(self) -> None:
        for name, value in sorted(self._items.items()):
            print(f"{name}: {value}")
if __name__ == '__main__':
    manager = ItemManager()
    sample_data = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "dark red")
    ]
    for name, value in sample_data:
        if not manager.add_item(name, value):
            print(f"Failed to add {name}")
    print("\nCurrent Inventory:")
    manager.list_items()
    update_target = "banana"
    new_color = "green"
    result = manager.update_item(update_target, new_color)
    if result:
        print(f"\nUpdated '{update_target}' to {new_color}")
    print("\nInventory after update:")
    manager.list_items()