class FindTheMiddleValueAmongThreeManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, value):
        self.entries.append(value)

    def update_entry(self, index, value):
        if 0 <= index < len(self.entries):
            self.entries[index] = value

    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = FindTheMiddleValueAmongThreeManager()
    manager.add_entry(1)
    manager.add_entry(3)
    manager.add_entry(2)
    print(manager.list_entries())
    manager.update_entry(1, 4)
    print(manager.list_entries())