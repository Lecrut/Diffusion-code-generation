class ItemStore:
    def __init__(self):
        self.items = set()

    def add(self, item):
        self.items.add(item)

    def check(self, item):
        return item in self.items

if __name__ == '__main__':
    store = ItemStore()
    sample_items = ["apple", "banana", "cherry"]
    for item in sample_items:
        store.add(item)
    print(store.check("banana"))
    print(store.check("grape"))