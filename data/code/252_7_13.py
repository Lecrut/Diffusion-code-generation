class CompareTwoSimpleQuantitiesNowManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        if not isinstance(entry, str) or len(entry.strip()) == 0:
            raise ValueError("Entry must be a non-empty string")
        self.entries.append(entry)

    def update_entry(self, index, new_entry):
        if not isinstance(index, int) or index < 0:
            raise ValueError("Index must be a non-negative integer")
        if not isinstance(new_entry, str) or len(new_entry.strip()) == 0:
            raise ValueError("New entry must be a non-empty string")
        if 0 <= index < len(self.entries):
            self.entries[index] = new_entry

    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = CompareTwoSimpleQuantitiesNowManager()
    manager.add_entry("Sample entry 1")
    manager.add_entry("Sample entry 2")
    manager.update_entry(0, "Updated sample entry 1")
    print(manager.list_entries())