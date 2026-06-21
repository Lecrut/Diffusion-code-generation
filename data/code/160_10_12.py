class ItemStore:
    def __init__(self):
        self.items = []
    
    def add_item(self, item_name: str):
        if isinstance(item_name, str) and item_name.strip():
            self.items.append(item_name)
    
    def get_items(self):
        return self.items.copy()

if __name__ == '__main__':
    store = ItemStore()
    store.add_item("apple")
    store.add_item("banana")
    print(store.get_items())