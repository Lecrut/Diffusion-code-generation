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
    sample_items = ['orange', 'grape', 'kiwi']
    item_list = ItemList()
    
    for item in sample_items:
        item_list.add_item(item)
    
    print("Added items:", item_list.items)
    
    removed_item = item_list.get_item(1)
    if removed_item is not None:
        print(f"Removed item at index 1: {removed_item}")
    else:
        print("Index out of range")
    
    item_list.remove_item(2)
    print("Remaining items:", item_list.items)