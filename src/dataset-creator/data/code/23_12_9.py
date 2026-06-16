class ItemRegistry:
    def __init__(self):
        self._data = {}
    def add(self, name, metadata=None):
        if not isinstance(metadata, dict) and metadata is None:
            metadata = {}
        self._data[name] = metadata
    def get(self, name):
        return self._data.get(name)
    def update(self, name, key, value):
        item = self._data.get(name)
        if item is not None and isinstance(item, dict):
            item[key] = value
    def remove(self, name):
        del self._data[name]
    def exists(self, name):
        return name in self._data
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_data = [
        ("apple", {"color": "red", "calories": 52}),
        ("banana", {"color": "yellow", "calories": 89}),
        ("orange", {"color": "orange", "calories": 47}),
    ]
    for name, meta in sample_data:
        registry.add(name, meta)
    print(f"Apple details: {registry.get('apple')}")
    registry.update("banana", "weight_kg", 0.12)
    print(f"Updated banana weight: {registry.get('banana')}" )