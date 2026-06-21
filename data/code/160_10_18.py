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
    sample_data = [
        "apple\n",
        "banana\n",
        "kiwi\n",
        "orange\n"
    ]
    for data in sample_data:
        store.add_item(data.strip())
    
    print(store.get_items())