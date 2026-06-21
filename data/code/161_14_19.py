class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not isinstance(item, str):
            raise ValueError("Item must be a string")
        self.items.append(item)

    def remove_item(self, index):
        if not isinstance(index, int) or index < 0:
            raise ValueError("Index must be a non-negative integer")
        if index >= len(self.items):
            raise IndexError("Index out of range")
        del self.items[index]

    def get_item(self, index):
        if not isinstance(index, int) or index < 0:
            raise ValueError("Index must be a non-negative integer")
        if index >= len(self.items):
            raise IndexError("Index out of range")
        return self.items[index]

if __name__ == '__main__':
    item_list = ItemList()
    item_list.add_item('apple')
    item_list.add_item('banana')
    print(item_list.get_item(0))
    item_list.remove_item(1)