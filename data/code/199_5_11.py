class NameFilter:
    def __init__(self):
        self.alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def filter_names(self, names):
        return [name for name in names if all(char in self.alphabet for char in name)]

if __name__ == '__main__':
    names = ['Alice', 'Bob', 'Charlie!', 'David']
    name_filter = NameFilter()
    filtered_names = name_filter.filter_names(names)
    print(filtered_names)