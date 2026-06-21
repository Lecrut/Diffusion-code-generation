class NameGrouping:
    def __init__(self):
        self.grouped_names = {}

    def add_name(self, name):
        first_letter = name[0].upper()
        if first_letter not in self.grouped_names:
            self.grouped_names[first_letter] = []
        self.grouped_names[first_letter].append(name)

    def get_grouped_names(self):
        return self.grouped_names

if __name__ == '__main__':
    grouping = NameGrouping()
    for name in ["Alice", "bob", "Charlie", "david", "eve"]:
        grouping.add_name(name)
    print(grouping.get_grouped_names())