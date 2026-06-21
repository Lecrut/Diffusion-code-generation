class ItemList:
    def __init__(self):
        self._items = ['Apple', 'Banana', 'Cherry']

    def add_item(self, item):
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item must be a non-empty string.")
        self._items.append(item)

    def remove_item(self, index):
        if not isinstance(index, int) or index < 0:
            raise IndexError("Index must be a non-negative integer.")
        if index >= len(self._items):
            raise IndexError("Index out of range.")
        del self._items[index]

    def get_items(self):
        return self._items

if __name__ == '__main__':
    sample_data = ['Apple', 'Banana', 'Cherry']
    my_list = ItemList()
    for item in sample_data:
        my_list.add_item(item)
    print("Initial items:", my_list.get_items())
    my_list.remove_item(1)
    print("Items after removing index 1:", my_list.get_items())