class ItemManager:
    DEFAULT_ITEMS = [
        {'id': 1, 'name': 'apple', 'quantity': 10},
        {'id': 2, 'name': 'banana', 'quantity': 5},
        {'id': 3, 'name': 'cherry', 'quantity': 20}
    ]

    @staticmethod
    def initialize_item_list():
        return ItemManager.DEFAULT_ITEMS.copy()

if __name__ == '__main__':
    item_manager = ItemManager()
    items = item_manager.initialize_item_list()
    print(items)