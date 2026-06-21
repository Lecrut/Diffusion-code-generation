class NameFilter:
    def __init__(self):
        self.alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def is_valid_name(self, name):
        return all(char in self.alphabet for char in name)

    def filter_names(self, names):
        return [name for name in names if self.is_valid_name(name)]

if __name__ == '__main__':
    filter_instance = NameFilter()
    sample_names = ['Alice', 'Bob', 'Charlie!', 'D@vid', 'Eve']
    valid_names = filter_instance.filter_names(sample_names)
    print(valid_names)