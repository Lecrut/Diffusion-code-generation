class ItemStore:
    def __init__(self):
        self.items = {}
    def add_item(self, name):
        self.items[name] = True
if __name__ == '__main__':
    store = ItemStore()
    store.add_item("Apple")
    store.add_item("Banana")
    store.add_item("Apple")
    store.add_item("Cherry")
    print(store.items)