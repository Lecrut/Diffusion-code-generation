class ItemStore:
    def __init__(self):
        self._items = set()
    def add_item(self, item_name):
        self._items.add(item_name)
    def get_items(self):
        return list(self._items)
if __name__ == '__main__':
    store = ItemStore()
    store.add_item("apple")
    store.add_item("banana")
    store.add_item("apple")
    store.add_item("orange")
    items = store.get_items()
    print(items)