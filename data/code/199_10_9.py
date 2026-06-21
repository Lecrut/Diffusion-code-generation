class NameFilter:
    MIN_LENGTH = 5

    @staticmethod
    def filter_names(names):
        return [name for name in names if len(name) > NameFilter.MIN_LENGTH]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "alice", "Bob"]
    filtered_names = NameFilter.filter_names(sample_names)
    print(filtered_names)