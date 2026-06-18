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
        removed = name in self._items
        if removed:
            del self._items[name]
        return removed
if __name__ == '__main__':
    manager = ItemManager()
    manager.add_item('apple', 'red')
    manager.add_item('banana', 'yellow')
    assert manager.get_item('apple') == 'red'
    assert manager.update_item('apple', 'green') is True
    print(manager._items)