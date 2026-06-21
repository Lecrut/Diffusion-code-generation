class ItemList:
    def __init__(self):
        self._items = ['apple', 'banana', 'cherry']

    def get_items(self):
        return self._items

if __name__ == '__main__':
    item_list = ItemList()
    print(item_list.get_items())