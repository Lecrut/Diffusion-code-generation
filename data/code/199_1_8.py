class NameFilter:
    def __init__(self, initial):
        self.initial = initial

    @staticmethod
    def filter_names(names, initial):
        return [name for name in names if name.startswith(initial)]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    initial_char = 'A'
    filter_instance = NameFilter(initial_char)
    filtered_names = filter_instance.filter_names(sample_names, initial_char)
    print(filtered_names)