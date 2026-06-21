class ItemList:

    def __init__(self):
        self.items = ['apple', 'banana', 'cherry']

    def get_item(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            return None
if __name__ == '__main__':
    item_list = ItemList()
    print(item_list.get_item(0))
    print(item_list.get_item(1))
    print(item_list.get_item(2))
    print(item_list.get_item(3))