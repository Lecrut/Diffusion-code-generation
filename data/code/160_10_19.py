class ItemStore:
    def __init__(self):
        self.items = []
    
    def add_item(self, item_name: str):
        if isinstance(item_name, str) and item_name.strip():
            self.items.append(item_name)
    
    def get_items(self) -> list:
        return self.items.copy()

if __name__ == '__main__':
    store = ItemStore()
    sample_items = ["apple", "banana", "cherry"]
    for item in sample_items:
        store.add_item(item)
    print(store.get_items())