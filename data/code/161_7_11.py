class ItemManager:
    ITEMS = {
        "apple": 100,
        "banana": 150,
        "cherry": 200
    }

    @staticmethod
    def get_item(key):
        return ItemManager.ITEMS.get(key, None)

if __name__ == '__main__':
    print(ItemManager.get_item("apple"))
    print(ItemManager.get_item("banana"))
    print(ItemManager.get_item("grape"))