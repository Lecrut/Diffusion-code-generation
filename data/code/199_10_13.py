class NameProcessor:
    MIN_LENGTH = 5

    @staticmethod
    def filter_names(names):
        return [name for name in names if len(name.strip()) > NameProcessor.MIN_LENGTH]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "alice", "Bob"]
    processed_names = NameProcessor.filter_names(sample_names)
    print(processed_names)