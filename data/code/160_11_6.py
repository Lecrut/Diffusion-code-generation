class UniqueItemStore:
    def __init__(self):
        self._items = []

    def add_item(self, item_name):
        if item_name not in self._items:
            self._items.append(item_name)

    def get_items(self):
        return self._items.copy()

if __name__ == '__main__':
    store = UniqueItemStore()
    store.add_item("apple")
    store.add_item("banana")
    store.add_item("apple")
    store.add_item("orange")
    items = store.get_items()
    print(items)