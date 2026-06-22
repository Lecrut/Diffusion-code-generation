class DetermineTheLargestNumberPresentManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, number):
        self.entries.append(number)

    def update_entry(self, index, number):
        if 0 <= index < len(self.entries):
            self.entries[index] = number

    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = DetermineTheLargestNumberPresentManager()
    manager.add_entry(12)
    manager.add_entry(7)
    manager.update_entry(0, 5)
    print(manager.list_entries())