class ItemList:
    DEFAULT_ITEMS = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

    def __init__(self):
        self._items = self.DEFAULT_ITEMS.copy()

    def display(self):
        for index, item in enumerate(self._items):
            print(f"{index + 1}. {item}")

if __name__ == '__main__':
    sample_data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    my_list = ItemList()
    my_list.display()