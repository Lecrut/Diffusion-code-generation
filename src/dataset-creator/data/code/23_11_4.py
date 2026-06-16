class ItemManager:
    def __init__(self):
        self._items = {}
    def add(self, name, value):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self._items[name] = value
    def get(self, name):
        return self._items.get(name)
    def update(self, name, new_value):
        try:
            if name in self._items:
                old_value = self._items.pop(name)
                self.add(name, new_value)
                print(f"Updated '{name}' from {old_value} to {new_value}")
            else:
                raise KeyError(f"No item found with key '{name}'.")
        except Exception as e:
            if isinstance(e, KeyError):
                raise
            raise
    def list_all(self):
        return dict(sorted(self._items.items()))
if __name__ == '__main__':
    manager = ItemManager()
    manager.add("apple", "red")
    manager.add("banana", "yellow")
    manager.add("cherry", "dark red")
    print("\n--- Current Inventory ---")
    for item in list(manager.list_all().keys()):
        val = manager.get(item)
        if isinstance(val, str):
            print(f"{item}: {val}")
    try:
        manager.update("banana", "green")
    except Exception as e:
        print(e)
    print("\n--- Updated Inventory ---")
    for item in list(manager.list_all().keys()):
        val = manager.get(item)
        if isinstance(val, str):
            print(f"{item}: {val}")