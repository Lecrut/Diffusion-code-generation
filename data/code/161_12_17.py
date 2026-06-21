ITEM_LIST_TITLE = 'Sample Item List'

class EnhancedItemList:

    def __init__(self):
        self._items = []

    def add_item(self, item_name, item_quantity):
        self._items.append((item_name, item_quantity))

    def list_items(self):
        print(ITEM_LIST_TITLE)
        for item in self._items:
            print(f'{item[0]}: {item[1]}')
if __name__ == '__main__':
    my_list = EnhancedItemList()
    my_list.add_item('Apple', 3)
    my_list.add_item('Banana', 5)
    my_list.list_items()