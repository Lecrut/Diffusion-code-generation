class ItemList:
    def __init__(self):
        self._items = ['orange', 'grape', 'kiwi']

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]

    def get_items(self):
        return self._items

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry']
    my_list = ItemList()
    for item in sample_data:
        my_list.add_item(item)
    
    print("Initial items:", my_list.get_items())
    my_list.remove_item(1)
    print("Items after removing index 1:", my_list.get_items())