class CompareTwoSimpleQuantitiesNowManager:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, entry):
        self.entries.append(entry)
    
    def update_entry(self, index, new_entry):
        if 0 <= index < len(self.entries):
            self.entries[index] = new_entry
    
    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = CompareTwoSimpleQuantitiesNowManager()
    manager.add_entry("Sample entry A")
    manager.add_entry("Sample entry B")
    
    intermediate_result = manager.list_entries()
    print(intermediate_result)
    
    manager.update_entry(0, "Updated sample entry A")
    
    final_result = manager.list_entries()
    print(final_result)