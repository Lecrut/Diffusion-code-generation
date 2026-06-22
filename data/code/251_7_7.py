class DetermineTheLargestNumberPresentManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, number):
        self.entries.append(number)

    def update_entry(self, index, new_number):
        if 0 <= index < len(self.entries):
            self.entries[index] = new_number

    def list_entries(self):
        return sorted(self.entries, reverse=True)

if __name__ == '__main__':
    manager = DetermineTheLargestNumberPresentManager()
    manager.add_entry(10)
    manager.add_entry(5)
    manager.update_entry(0, 20)
    print(manager.list_entries())