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
        return None
if __name__ == '__main__':
    item_list = ItemList()
    item_list.add('apple')
    item_list.add('banana')
    print(item_list.get_by_index(0))
    item_list.remove(1)
    print(item_list.get_by_index(1))