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
    sample_items = ['orange', 'grape', 'pineapple']
    item_list = ItemList()
    for item in sample_items:
        item_list.add_item(item)
    
    print("First item:", item_list.get_item(0))
    item_list.remove_item(1)
    print("Item list after removal:", item_list.items)