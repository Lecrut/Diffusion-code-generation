class ItemStore:
    def __init__(self):
        self.items = {}
    def add_item(self, name, description):
        self.items[name] = (name, description)
    def get_item(self, name):
        return self.items.get(name)
if __name__ == '__main__':
    store = ItemStore()
    store.add_item("Apple", "A sweet red fruit.")
    store.add_item("Banana", "A long yellow fruit.")
    store.add_item("Carrot", "An orange root vegetable.")
    print(store.get_item("Apple"))
    print(store.get_item("Banana"))
    print(store.get_item("Grape"))