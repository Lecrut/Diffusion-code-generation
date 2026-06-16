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
            raise TypeError("Item name must be a string.")
        return self._items.get(name)
    def update_item(self, name: str, new_value: str) -> bool:
        current = self.get_item(name)
        if current is None:
            return False
        if not isinstance(new_value, str):
            raise TypeError("New item value must be a string.")
        self._items[name] = new_value
        return True
    def remove_item(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        removed = self._items.pop(name, None) is not None
        return removed
if __name__ == '__main__':
    manager = ItemManager()
    sample_data = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "dark red")
    ]
    for name, value in sample_data:
        result = manager.add_item(name, value)
        print(f"Added {name}: {result}")
    updated_value = "ripe banana"
    update_result = manager.update_item("banana", updated_value)
    print(f"Updated 'banana' to '{updated_value}': {update_result}")
    retrieved_apple = manager.get_item("apple")
    print(f"Retrieved apple: {retrieved_apple}")
    removed_cherry = manager.remove_item("cherry")
    print(f"Removed cherry: {removed_cherry}")
    final_check = manager.get_item("banana")
    print(f"Final banana value: {final_check}")