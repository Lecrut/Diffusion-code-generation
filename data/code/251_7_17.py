class DetermineTheLargestNumberPresentManager:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, number):
        if not isinstance(number, (int, float)):
            raise ValueError("Entry must be a number")
        self.entries.append(number)
    
    def update_entry(self, index, number):
        if not isinstance(index, int) or index < 0:
            raise IndexError("Index must be a non-negative integer")
        if not isinstance(number, (int, float)):
            raise ValueError("Entry must be a number")
        if index >= len(self.entries):
            raise IndexError("Index out of range")
        self.entries[index] = number
    
    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = DetermineTheLargestNumberPresentManager()
    manager.add_entry(10)
    manager.add_entry(20)
    manager.update_entry(0, 30)
    print(manager.list_entries())