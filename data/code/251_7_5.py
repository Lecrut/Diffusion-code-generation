class DetermineTheLargestNumberPresentManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, number):
        self.entries.append(number)

    def update_entry(self, old_number, new_number):
        if old_number in self.entries:
            index = self.entries.index(old_number)
            self.entries[index] = new_number

    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = DetermineTheLargestNumberPresentManager()
    manager.add_entry(10)
    manager.add_entry(20)
    manager.update_entry(10, 30)
    print(manager.list_entries())