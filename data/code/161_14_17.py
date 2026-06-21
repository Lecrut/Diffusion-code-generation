class ItemList:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]

    def get(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        return None
if __name__ == '__main__':
    il = ItemList()
    il.add('apple')
    il.add('banana')
    print(il.get(0))
    il.remove(1)
    print(il.get(1))