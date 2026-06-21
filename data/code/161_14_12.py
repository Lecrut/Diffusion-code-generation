class ItemList:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
    
    def get_item(self, index):
        return self.items[index] if 0 <= index < len(self.items) else None

if __name__ == '__main__':
    item_list = ItemList()
    item_list.add_item('apple')
    item_list.add_item('banana')
    print(item_list.get_item(0))
    item_list.remove_item(1)