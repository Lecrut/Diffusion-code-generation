class ItemInitializer:
    DEFAULT_ITEMS = [
        {"name": "apple", "type": "fruit"},
        {"name": "banana", "type": "fruit"},
        {"name": "cherry", "type": "fruit"},
        {"name": "date", "type": "fruit"}
    ]

    @staticmethod
    def initialize_item_list() -> list:
        return ItemInitializer.DEFAULT_ITEMS.copy()

if __name__ == '__main__':
    item_list = ItemInitializer.initialize_item_list()
    print(item_list)