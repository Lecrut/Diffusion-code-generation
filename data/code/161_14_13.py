class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not isinstance(item, str):
            raise ValueError("Item must be a string")
        self.items.append(item)

    def remove_item(self, index):
        if not isinstance(index, int) or index < 0:
            raise IndexError("Index must be a non-negative integer")
        if index >= len(self.items):
            raise IndexError("Index out of range")
        del self.items[index]

    def get_item(self, index):
        if not isinstance(index, int) or index < 0:
            raise IndexError("Index must be a non-negative integer")
        if index >= len(self.items):
            raise IndexError("Index out of range")
        return self.items[index]

if __name__ == '__main__':
    il = ItemList()
    il.add_item('apple')
    il.add_item('banana')
    print(il.get_item(0))
    try:
        il.remove_item(1)
    except IndexError as e:
        print(e)