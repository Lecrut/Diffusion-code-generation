class ItemManager:
    DEFAULT_ITEMS = [
        {'id': 1, 'name': 'Apple', 'price': 0.99},
        {'id': 2, 'name': 'Banana', 'price': 0.59},
        {'id': 3, 'name': 'Cherry', 'price': 2.49}
    ]

    @staticmethod
    def populate_items():
        return ItemManager.DEFAULT_ITEMS

if __name__ == '__main__':
    manager = ItemManager()
    items = manager.populate_items()
    print("List of items:")
    for item in items:
        print(item)