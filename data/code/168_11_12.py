class StringCategorizer:
    def __init__(self):
        self.groups = {}

    def add_string(self, string):
        key = string[0]
        if key not in self.groups:
            self.groups[key] = []
        self.groups[key].append(string)

    def get_groups(self):
        return dict(sorted(self.groups.items()))

if __name__ == '__main__':
    categorizer = StringCategorizer()
    strings = ['apple', 'banana', 'avocado', 'cherry', 'blueberry']
    for string in strings:
        categorizer.add_string(string)
    print(categorizer.get_groups())