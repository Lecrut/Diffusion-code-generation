class ItemList:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def list_items(self):
        return self.items

if __name__ == '__main__':
    my_list = ItemList()
    sample_items = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry"
    ]
    for item in sample_items:
        my_list.add_item(item)
    
    print("Initial list of items:")
    print(my_list.list_items())
    
    my_list.remove_item("banana")
    print("\nAfter removing 'banana':")
    print(my_list.list_items())