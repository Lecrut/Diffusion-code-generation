class ItemStore:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name):
        self.items[item_name] = item_name
if __name__ == '__main__':
    store = ItemStore()
    store.add_item("apple")
    store.add_item("banana")
    store.add_item("cherry")
    print(store.items)