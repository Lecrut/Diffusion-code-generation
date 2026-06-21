class ItemList:
    DEFAULT_ITEMS = ['Apple', 'Banana', 'Cherry']

    def __init__(self, items=DEFAULT_ITEMS):
        self._items = [item.strip().capitalize() for item in items]

    def add_item(self, item):
        if item not in self._items:
            self._items.append(item.capitalize())

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]

    def get_items(self):
        return self._items.copy()

    @staticmethod
    def is_valid_item_name(name):
        return name.strip().isalpha() and name[0].isupper()

if __name__ == '__main__':
    sample_data = ["apple", "Banana", "Cherry", "date"]
    my_list = ItemList(sample_data)
    print("Initial items:", my_list.get_items())
    my_list.add_item('grape')
    print("Items after adding 'Grape':", my_list.get_items())
    my_list.remove_item(1)
    print("Items after removing index 1:", my_list.get_items())