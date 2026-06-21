class ListModifier:
    def __init__(self, initial_list):
        self.items = list(initial_list)
    
    def remove_by_index(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
    
    def remove_by_value(self, value):
        if value in self.items:
            self.items.remove(value)

if __name__ == '__main__':
    initial_data = ["apple", "banana", "apple", "orange", "banana"]
    modifier = ListModifier(initial_data)
    print("Initial list:", modifier.items)
    
    modifier.remove_by_value("apple")
    print(f"After removing first 'apple':", modifier.items)
    
    modifier.remove_by_index(2)
    print(f"After removing item at index 2:", modifier.items)