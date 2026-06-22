class FindTheMiddleValueAmongThreeManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Entry must be a number.")
        self.entries.append(value)

    def update_entry(self, index, value):
        if not isinstance(index, int) or index < 0:
            raise IndexError("Index must be a non-negative integer.")
        if not isinstance(value, (int, float)):
            raise ValueError("Entry must be a number.")
        if 0 <= index < len(self.entries):
            self.entries[index] = value

    def list_entries(self):
        return sorted(self.entries)

if __name__ == '__main__':
    manager = FindTheMiddleValueAmongThreeManager()
    manager.add_entry(5)
    manager.add_entry(2)
    manager.add_entry(8)
    print(manager.list_entries())
    manager.update_entry(1, 4)
    print(manager.list_entries())