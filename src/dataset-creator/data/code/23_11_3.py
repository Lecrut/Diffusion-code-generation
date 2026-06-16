class ItemManager:
    def __init__(self) -> None:
        self._items: dict[str, str] = {}
    def add_item(self, name: str, value: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name.strip()) == 0:
            return False
        self._items[name.strip()] = value.strip()
        return True
    def get_item(self, name: str) -> str | None:
        normalized_name = name.strip().lower()
        for key in list(self._keys()):
            if key.lower() == normalized_name:
                return self._items[key]
        return None
    def update_item(self, old_name: str, new_value: str) -> bool:
        existing_key = next((k for k in self.keys() if k.strip().lower() == old_name.strip().lower()), None)
        if not existing_key:
            raise KeyError(f"Item '{old_name}' not found.")
        self._items[existing_key] = new_value.strip()
        return True
    def keys(self):
        yield from self._keys()
    def _keys(self):
        for key in list(self._items.keys()):
            if isinstance(key, str) and len(key.strip()) > 0:
                yield key
if __name__ == '__main__':
    manager = ItemManager()
    assert manager.add_item("apple", "red") is True
    assert manager.get_item("Apple") == "red"
    assert manager.update_item("apple", "green") is True
    print(manager.get_item("APPLE"))