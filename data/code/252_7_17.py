class CompareTwoSimpleQuantitiesNowManager:
    DEFAULT_ENTRIES = [
        ("Sample entry 1", "value1"),
        ("Sample entry 2", "value2")
    ]

    def __init__(self):
        self.entries = self.DEFAULT_ENTRIES.copy()

    @staticmethod
    def create_entry(quantity1, quantity2):
        return (quantity1, quantity2)

    def add_entry(self, quantity1, quantity2):
        new_entry = CompareTwoSimpleQuantitiesNowManager.create_entry(quantity1, quantity2)
        self.entries.append(new_entry)

    def update_entry(self, index, quantity1, quantity2):
        if 0 <= index < len(self.entries):
            self.entries[index] = CompareTwoSimpleQuantitiesNowManager.create_entry(quantity1, quantity2)

    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = CompareTwoSimpleQuantitiesNowManager()
    manager.add_entry("Quantity A", "Value A")
    manager.update_entry(0, "Updated Quantity B", "Updated Value B")
    print(manager.list_entries())