class ItemList:
    _INITIAL_ITEMS = ['Apple', 'Banana', 'Cherry']

    def __init__(self):
        self._items = self._INITIAL_ITEMS.copy()

    @staticmethod
    def _display_item(item, index):
        print(f"{index + 1}. {item}")

    def display(self):
        for index, item in enumerate(self._items):
            ItemList._display_item(item, index)

if __name__ == '__main__':
    my_list = ItemList()
    my_list.display()