class DynamicItemStore:
    def __init__(self):
        self._items = {}
    def add(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._items[name] = True
    def get_all_names(self) -> list[str]:
        return sorted(list(self._items.keys()))
    def remove(self, name: str) -> bool:
        if name in self._items:
            del self._items[name]
            return True
        return False
    def contains(self, name: str) -> bool:
        return name in self._items
if __name__ == '__main__':
    store = DynamicItemStore()
    sample_items = ["apple", "banana", "cherry"]
    for item in sample_items:
        store.add(item)
    print("Current items:", store.get_all_names())
    if not store.contains("banana"):
        store.remove("banana")
    print("After removal:", store.get_all_names())