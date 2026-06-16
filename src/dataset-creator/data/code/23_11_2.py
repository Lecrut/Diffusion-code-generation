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
            return False
        self._items[name] = new_value
        return True
if __name__ == '__main__':
    manager = ItemManager()
    sample_data = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "dark red")
    ]
    for name, value in sample_data:
        result = manager.add_item(name=name, value=value)
        print(f"Added {name}: {result}")
    updated_value = "green"
    update_result = manager.update_item("apple", new_value=updated_value)
    print(f"Updated apple to '{updated_value}': {update_result}")
    retrieved_apple = manager.get_item("apple")
    print(f"Retrieved apple: {retrieved_apple}")