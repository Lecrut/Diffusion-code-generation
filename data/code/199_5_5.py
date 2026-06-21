class NameFilter:
    def __init__(self):
        self.alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def filter_names(self, names):
        return [name for name in names if all(char in self.alphabet for char in name)]

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie!', 'D@vid', 'Eve']
    filterer = NameFilter()
    filtered_names = filterer.filter_names(sample_names)
    print(filtered_names)