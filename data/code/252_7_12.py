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
    print(manager.list_entries())
    manager.update_entry(0, "Updated sample entry A")
    print(manager.list_entries())