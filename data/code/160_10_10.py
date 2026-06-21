class ItemStore:
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str):
        if isinstance(item_name, str) and item_name.strip():
            self.items.append(item_name)

    def get_items(self):
        return self.items

if __name__ == '__main__':
    store = ItemStore()
    store.add_item("Apple")
    store.add_item("Banana")
    print(store.get_items())