class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item must be a non-empty string")
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items:
            raise ValueError("Item not found in the list")
        self.items.remove(item)

    def list_items(self):
        return self.items.copy()

if __name__ == '__main__':
    my_list = ItemList()
    try:
        my_list.add_item('apple')
        my_list.add_item('banana')
        print(my_list.list_items())
        my_list.remove_item('apple')
        print(my_list.list_items())
        my_list.remove_item('orange')
    except ValueError as e:
        print(e)