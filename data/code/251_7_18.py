class DetermineTheLargestNumberPresentManager:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, number):
        self.entries.append(number)
    
    def update_entry(self, index, number):
        if 0 <= index < len(self.entries):
            self.entries[index] = number
    
    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = DetermineTheLargestNumberPresentManager()
    manager.add_entry(5)
    manager.add_entry(15)
    manager.update_entry(0, 25)
    entries = manager.list_entries()
    max_value = -float('inf')
    for num in entries:
        if num > max_value:
            max_value = num
    print(max_value)