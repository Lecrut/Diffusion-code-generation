class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def list_items(self):
        return self.items.copy()

if __name__ == '__main__':
    my_list = ItemList()
    my_list.add_item('apple')
    my_list.add_item('banana')
    print("Current items:", my_list.list_items())
    my_list.remove_item('apple')
    print("Items after removal:", my_list.list_items())