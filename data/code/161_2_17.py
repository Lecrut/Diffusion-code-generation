class ItemList:
    def __init__(self):
        self._items = ['Apple', 'Banana', 'Cherry']

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]

    def display(self):
        for index, item in enumerate(self._items):
            print(f"{index + 1}. {item}")

if __name__ == '__main__':
    my_list = ItemList()
    my_list.display()
    my_list.add_item('Date')
    my_list.display()
    my_list.remove_item(0)
    my_list.display()