class UniqueItemStore:
    def __init__(self):
        self._seen = set()
        self._order = []

    def add_item(self, item_name):
        if item_name not in self._seen:
            self._seen.add(item_name)
            self._order.append(item_name)

    def get_items(self):
        return self._order

if __name__ == '__main__':
    store = UniqueItemStore()
    store.add_item("apple")
    store.add_item("banana")
    store.add_item("apple")
    store.add_item("orange")
    items = store.get_items()
    print(items)