class ItemStore:
    def __init__(self):
        self._items = {}
    def add_item(self, item_name):
        self._items[item_name] = item_name
    def get_item(self, item_name):
        return self._items.get(item_name)
if __name__ == '__main__':
    store = ItemStore()
    store.add_item("apple")
    store.add_item("banana")
    store.add_item("cherry")
    print(store.get_item("apple"))
    print(store.get_item("grape"))