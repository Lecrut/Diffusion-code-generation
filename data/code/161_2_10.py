class ItemList:
    DEFAULT_ITEMS = ["Apple", "Banana", "Cherry"]

    def __init__(self, items=DEFAULT_ITEMS):
        self._items = items

    @staticmethod
    def _format_item(index, item):
        return f"{index + 1}. {item}"

    def display(self):
        for index, item in enumerate(self._items):
            print(ItemList._format_item(index, item))

if __name__ == '__main__':
    sample_data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    my_list = ItemList(sample_data)
    my_list.display()