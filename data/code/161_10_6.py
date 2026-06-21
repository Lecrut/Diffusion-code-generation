class ItemList:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def list_items(self):
        return self.items.copy()

if __name__ == '__main__':
    my_list = ItemList()
    my_list.add('apple')
    my_list.add('banana')
    print(my_list.list_items())
    my_list.remove('apple')
    print(my_list.list_items())