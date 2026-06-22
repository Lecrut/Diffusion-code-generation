class DetermineTheLargestNumberPresentManager:
    MAX_VALUE = -float('inf')

    def __init__(self):
        self.entries = []

    def add_entry(self, number):
        if number > DetermineTheLargestNumberPresentManager.MAX_VALUE:
            DetermineTheLargestNumberPresentManager.MAX_VALUE = number
        self.entries.append(number)

    def update_entry(self, index, number):
        if 0 <= index < len(self.entries) and number > DetermineTheLargestNumberPresentManager.MAX_VALUE:
            DetermineTheLargestNumberPresentManager.MAX_VALUE = number
        if 0 <= index < len(self.entries):
            self.entries[index] = number

    def list_entries(self):
        return self.entries, DetermineTheLargestNumberPresentManager.MAX_VALUE

if __name__ == '__main__':
    manager = DetermineTheLargestNumberPresentManager()
    manager.add_entry(10)
    manager.add_entry(20)
    manager.update_entry(0, 30)
    entries, max_value = manager.list_entries()
    print(entries)
    print(max_value)