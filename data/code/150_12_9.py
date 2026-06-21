class ItemList:
    def __init__(self, initial_list):
        self.items = list(initial_list)
    
    def remove_by_index(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
    
    def remove_by_value(self, value):
        if value in self.items:
            self.items.remove(value)

if __name__ == '__main__':
    initial_data = ["apple", "banana", "cherry", "date"]
    item_list = ItemList(initial_data)
    print("Initial list:", item_list.items)
    
    item_list.remove_by_index(1)
    print("After removing index 1:", item_list.items)
    
    item_list.remove_by_value("cherry")
    print("After removing value 'cherry':", item_list.items)