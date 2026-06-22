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
    manager.add_entry("Entry 1")
    manager.add_entry("Entry 2")
    manager.update_entry(0, "Updated Entry 1")
    print(manager.list_entries())