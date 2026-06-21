class ItemListInitializer:
    @staticmethod
    def create_item_list():
        return [
            {"id": 1, "name": "apple", "quantity": 10},
            {"id": 2, "name": "banana", "quantity": 20},
            {"id": 3, "name": "cherry", "quantity": 30},
            {"id": 4, "name": "date", "quantity": 40}
        ]

if __name__ == '__main__':
    item_list = ItemListInitializer.create_item_list()
    print(item_list)