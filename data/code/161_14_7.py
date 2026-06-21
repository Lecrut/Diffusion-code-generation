class ItemList:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]

    def get_by_index(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        raise IndexError('Index out of range')
if __name__ == '__main__':
    il = ItemList()
    il.add('apple')
    il.add('banana')
    print(il.get_by_index(0))
    il.remove(1)
    try:
        print(il.get_by_index(1))
    except IndexError as e:
        print(e)