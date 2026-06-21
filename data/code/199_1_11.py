class NameFilter:
    @staticmethod
    def filter_names(names, initial):
        return [name for name in names if name.startswith(initial)]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    initial_char = 'A'
    filtered_names = NameFilter.filter_names(sample_names, initial_char)
    print(filtered_names)