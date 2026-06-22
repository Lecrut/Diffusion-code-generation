class FindTheMiddleValueAmongThreeManager:
    def __init__(self):
        self.entries = {}
    
    def add_entry(self, key, value):
        if 1 <= len(value) != 3:
            raise ValueError("Input list must contain exactly three numbers.")
        self.entries[key] = sorted(value)
    
    def update_entry(self, key, value):
        if key not in self.entries or len(value) != 3:
            raise ValueError("Invalid key or input list must contain exactly three numbers.")
        self.entries[key] = sorted(value)
    
    def get_median(self, key):
        if key not in self.entries:
            raise KeyError("Key not found.")
        return self.entries[key][1]
    
    def list_entries(self):
        return {key: (entry[0], entry[-1]) for key, entry in self.entries.items()}

if __name__ == '__main__':
    manager = FindTheMiddleValueAmongThreeManager()
    manager.add_entry('sample1', [5, 2, 8])
    print(manager.get_median('sample1'))
    
    manager.update_entry('sample1', [3, 7, 4])
    print(manager.get_median('sample1'))
    
    print(manager.list_entries())