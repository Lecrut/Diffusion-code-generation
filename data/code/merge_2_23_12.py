class ItemRegistry:
    def __init__(self):
        self._data = {}
    def add(self, name, metadata=None):
        if not isinstance(metadata, dict):
            raise ValueError("Metadata must be a dictionary")
        self._data[name] = metadata
    def get(self, name):
        return self._data.get(name)
    def remove(self, name):
        return self._data.pop(name, None)
    def contains(self, name):
        return name in self._data
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_items = [
        ("apple", {"color": "red", "calories": 52}),
        ("banana", {"color": "yellow", "calories": 89}),
        ("orange", {"color": "orange", "calories": 47})
    ]
    for name, meta in sample_items:
        registry.add(name, meta)
    print("Registered items:", list(registry._data.keys()))
    if registry.contains("banana"):
        item = registry.get("banana")
        print(f"Found banana with metadata: {item}")
        del_item = registry.remove("orange")
        print(f"Removed orange, original data was: {del_item}")
    assert not registry.contains("orange"), "Orange should be removed"
    try:
        _ = registry.get("grape")
    except KeyError:
        pass                     
    print("All operations completed successfully.")