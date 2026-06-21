class ItemStore:
    def __init__(self, initial_items=None):
        if initial_items is None:
            self.items = set()
        else:
            try:
                self.items = set(initial_items)
            except TypeError as e:
                raise ValueError("Initial items must be iterable") from e

    def add(self, item):
        self.items.add(item)

    def check(self, item):
        return item in self.items

if __name__ == '__main__':
    store = ItemStore(["apple", "banana", "cherry"])
    print(store.check("apple"))
    print(store.check("date"))
    store.add("date")
    print(store.check("date"))