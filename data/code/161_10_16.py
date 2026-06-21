class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item must be a non-empty string")
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise KeyError(f"Item '{item}' not found")

    def list_items(self):
        return self.items.copy()

if __name__ == '__main__':
    my_list = ItemList()
    my_list.add_item('apple')
    my_list.add_item('banana')
    print(my_list.list_items())
    try:
        my_list.remove_item('apple')
        print(my_list.list_items())
        my_list.remove_item('grape')
    except KeyError as e:
        print(e)