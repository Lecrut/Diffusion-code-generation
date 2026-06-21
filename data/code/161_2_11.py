class ItemList:
    ITEMS = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

    def __init__(self):
        self._items = self.ITEMS.copy()

    def display(self):
        for index, item in enumerate(self._items, start=1):
            print(f"{index}. {item}")

if __name__ == '__main__':
    my_list = ItemList()
    my_list.display()