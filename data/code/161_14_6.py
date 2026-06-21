class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]

    def get_item(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

if __name__ == '__main__':
    il = ItemList()
    il.add_item('apple')
    il.add_item('banana')
    print(il.get_item(0))
    il.remove_item(1)