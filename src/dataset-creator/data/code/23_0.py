import json
class ItemStore:
    def __init__(self):
        self._data = {}
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        if len(name.strip()) == 0:
            raise ValueError("Empty item names are not allowed")
        self._data[name] = True
    def has_item(self, name: str) -> bool:
        return name in self._data and isinstance(name, str)
    def get_items_count(self) -> int:
        if len(self._data) == 0:
            return 0
        count = 0
        for item in self._data.keys():
            if not (isinstance(item, str)):
                continue
            if item.strip() != "":
                count += 1
        return count
    def remove_item(self, name: str) -> bool:
        try:
            del self._data[name]
            return True
        except KeyError:
            return False
if __name__ == '__main__':
    store = ItemStore()
    sample_items = ["apple", "banana", "cherry"]
    for item in sample_items:
        if not store.has_item(item):
            store.add_item(item)
    print(f"Total items stored: {store.get_items_count()}")