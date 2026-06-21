class NameGroup:
    def __init__(self):
        self.groups = {}

    def add_name(self, name):
        first_letter = name[0].upper()
        if first_letter not in self.groups:
            self.groups[first_letter] = []
        self.groups[first_letter].append(name)

    def get_groups(self):
        return self.groups

if __name__ == '__main__':
    names = ["Alice", "bob", "Charlie", "david", "eve"]
    name_group = NameGroup()
    for name in names:
        name_group.add_name(name)
    
    grouped_names = name_group.get_groups()
    print(grouped_names)