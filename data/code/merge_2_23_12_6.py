class ItemRegistry:
    def __init__(self):
        self._data = {}
    def add_item(self, name, metadata=None):
        if not isinstance(metadata, dict):
            raise TypeError("Metadata must be a dictionary")
        self._data[name] = metadata
    def get_item(self, name):
        return self._data.get(name)
    def remove_item(self, name):
        return self._data.pop(name, None)
    def update_metadata(self, name, new_metadata=None):
        if not isinstance(new_metadata, dict):
            raise TypeError("New metadata must be a dictionary")
        item = self._data.get(name)
        if item is None:
            return False
        for key in new_metadata.keys():
            item[key] = new_metadata[key]
        return True
    def __repr__(self):
        return f"ItemRegistry({list(self._data.keys())})"
if __name__ == '__main__':
    registry = ItemRegistry()
    registry.add_item("apple", {"color": "red", "calories": 52})
    registry.add_item("banana", {"color": "yellow", "calories": 89})
    print(registry.get_item("apple"))
    updated = registry.update_metadata("apple", {"weight": "medium"})
    print(updated)
    removed = registry.remove_item("banana")
    print(removed)
    print(registry)