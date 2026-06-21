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
        return sorted(self.items)

if __name__ == '__main__':
    my_list = ItemList()
    my_list.add_item('banana')
    my_list.add_item('apple')
    my_list.add_item('cherry')
    print("Initial items:", my_list.list_items())
    my_list.remove_item('banana')
    print("Items after removing banana:", my_list.list_items())