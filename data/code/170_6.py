class ItemStorage:
    def __init__(self):
        self.items = []
    def add_item(self, item_data):
        self.items.append(item_data)
    def get_all_items(self):
        return self.items
if __name__ == '__main__':
    storage = ItemStorage()
    item1 = {"id": 1, "name": "Apple", "quantity": 10}
    item2 = {"id": 2, "name": "Banana", "quantity": 5}
    item3 = {"id": 3, "name": "Orange", "quantity": 12}
    storage.add_item(item1)
    storage.add_item(item2)
    storage.add_item(item3)
    all_items = storage.get_all_items()
    print(all_items)