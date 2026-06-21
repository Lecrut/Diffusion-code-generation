class ItemManager:
    ITEM_DATA = [
        {'id': 1, 'name': 'Apple', 'price': 0.99},
        {'id': 2, 'name': 'Banana', 'price': 0.59},
        {'id': 3, 'name': 'Cherry', 'price': 2.49}
    ]

    @staticmethod
    def get_items():
        return ItemManager.ITEM_DATA

if __name__ == '__main__':
    items = ItemManager.get_items()
    for item in items:
        print(item)