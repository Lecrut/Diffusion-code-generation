class NameFilter:
    def __init__(self, names):
        self.names = names

    def filter_names(self):
        alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return [name for name in self.names if all(char in alphabet for char in name)]

if __name__ == '__main__':
    names = ["Alice", "Bob", "Charlie!", "David"]
    name_filter = NameFilter(names)
    filtered_names = name_filter.filter_names()
    print(filtered_names)