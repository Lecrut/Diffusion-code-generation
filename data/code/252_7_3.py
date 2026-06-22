class CompareTwoSimpleQuantitiesNowManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, quantity1, quantity2):
        self.entries.append((quantity1, quantity2))

    def update_entry(self, index, quantity1, quantity2):
        if 0 <= index < len(self.entries):
            self.entries[index] = (quantity1, quantity2)

    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = CompareTwoSimpleQuantitiesNowManager()
    manager.add_entry(5, 3)
    manager.update_entry(0, 7, 4)
    print(manager.list_entries())