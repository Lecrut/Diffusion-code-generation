class ItemStore:
    def __init__(self):
        self.items = {}
    def add_item(self, name):
        self.items[name] = name
if __name__ == '__main__':
    store = ItemStore()
    print(f"Initial store: {store.items}")
    store.add_item("Apple")
    store.add_item("Banana")
    store.add_item("Apple")
    store.add_item("Cherry")
    print(f"Store after adding items: {store.items}")