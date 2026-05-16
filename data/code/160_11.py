class ItemStore:
    def __init__(self):
        self._items = set()
    def add_item(self, item_name):
        self._items.add(item_name)
    def get_items(self):
        return list(self._items)
if __name__ == '__main__':
    store = ItemStore()
    store.add_item("Apple")
    store.add_item("Banana")
    store.add_item("Cherry")
    store.add_item("Apple")
    store.add_item("Date")
    items = store.get_items()
    print(items)