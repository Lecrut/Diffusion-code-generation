class ItemRegistry:
    def __init__(self):
        self._data = {}
    def add_item(self, name, metadata=None):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Item name must be a non-empty string.")
        item_data = {
            "name": name.strip(),
            "metadata": metadata.copy() if metadata else {}
        }
        self._data[name] = item_data
    def get_item(self, name):
        return self._data.get(name)
    def update_metadata(self, name, key, value):
        item = self.get_item(name)
        if not item:
            raise KeyError(f"Item '{name}' not found.")
        try:
            item["metadata"][key] = value
        except TypeError as e:
            raise ValueError("Metadata must be a dictionary.") from e
    def remove_item(self, name):
        return self._data.pop(name) if name in self._data else None
    def list_items(self):
        return list(self._data.keys())
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_data = [
        ("apple", {"color": "red", "calories": 52}),
        ("banana", {"color": "yellow", "calories": 89}),
        ("cherry", {"color": "dark red", "calories": 41})
    ]
    for name, meta in sample_data:
        registry.add_item(name, meta)
    print("Registered items:", registry.list_items())
    if "apple" in registry._data:
        registry.update_metadata("apple", "calories", 60)
    apple_info = registry.get_item("apple")
    print(f"\nItem 'apple' details:")
    for k, v in apple_info.items():
        if isinstance(v, dict):
            print(f"  {k}: {v}")
        else:
            print(f"  {k}: {v}")
    removed = registry.remove_item("banana")
    print("\nRemoved 'banana'. Remaining items:", registry.list_items())