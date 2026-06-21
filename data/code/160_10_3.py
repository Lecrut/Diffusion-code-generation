class ItemStore:
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str):
        if not isinstance(item_name, str) or not item_name.strip():
            raise ValueError("Item name must be a non-empty string")
        self.items.append(item_name)

    def get_items(self):
        return self.items.copy()

if __name__ == '__main__':
    store = ItemStore()
    store.add_item("apple")
    store.add_item("banana")
    print(store.get_items())