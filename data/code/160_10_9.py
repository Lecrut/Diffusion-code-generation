class ItemStore:
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str):
        if not item_name.strip():
            return
        self.items.append(item_name)

    def get_items(self) -> list:
        return self.items.copy()

if __name__ == '__main__':
    store = ItemStore()
    store.add_item("apple")
    store.add_item("banana")
    print(store.get_items())