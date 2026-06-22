class FindTheMiddleValueAmongThreeManager:
    def __init__(self):
        self.entries = {}
    
    def add_entry(self, key, value):
        self.entries[key] = value
    
    def update_entry(self, key, value):
        if key in self.entries:
            self.entries[key] = value
    
    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = FindTheMiddleValueAmongThreeManager()
    manager.add_entry('sample1', [5, 2, 8])
    manager.update_entry('sample1', [7, 3, 9])
    print(manager.list_entries())