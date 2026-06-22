class CompareTwoSimpleQuantitiesNowManager:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, entry):
        if not isinstance(entry, str):
            raise ValueError("Entry must be a string")
        self.entries.append(entry)
    
    def update_entry(self, index, new_entry):
        if not isinstance(new_entry, str):
            raise ValueError("New entry must be a string")
        if 0 <= index < len(self.entries):
            self.entries[index] = new_entry
        else:
            raise IndexError("Index out of range")
    
    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = CompareTwoSimpleQuantitiesNowManager()
    manager.add_entry("Sample entry 1")
    try:
        manager.add_entry(123)
    except ValueError as e:
        print(e)
    manager.update_entry(0, "Updated sample entry 1")
    try:
        manager.update_entry(5, "Another updated entry")
    except IndexError as e:
        print(e)
    print(manager.list_entries())