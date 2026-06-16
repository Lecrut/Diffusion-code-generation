class ItemManager:
    def __init__(self) -> None:
        self._items: dict[str, str] = {}
    def add_item(self, name: str, value: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(value, str):
            raise TypeError("Value must be a string.")
        self._items[name] = value
        return True
    def get_item(self, name: str) -> str | None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        return self._items.get(name)
    def update_item(self, name: str, new_value: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(new_value, str):
            raise TypeError("Value must be a string.")
        self._items[name] = new_value
        return True
    def remove_item(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        removed = name in self._items
        if removed:
            del self._items[name]
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
    retrieved_apple = manager.get_item("apple")
    print(f"Retrieved apple: {retrieved_apple}")
    updated_banana = "green"
    update_result = manager.update_item("banana", updated_banana)
    print(f"Updated banana to {updated_banana}: {update_result}")
    final_check = manager.get_item("banana")
    print(f"Final check for banana: {final_check}")
    remove_cherry = manager.remove_item("cherry")
    print(f"Removed cherry: {remove_cherry}")
    try_get_missing = manager.get_item("grape")
    print(f"Missing item (grape): {try_get_missing}")