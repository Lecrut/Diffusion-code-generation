class DictionaryProcessor:
    def __init__(self, data):
        self.data = data

    def print_large_values(self):
        for key, value in self.data.items():
            if value > 10:
                print(f"{key}: {value}")

if __name__ == '__main__':
    sample_dict = {
        'a': 5,
        'b': 12,
        'c': 8,
        'd': 15
    }
    processor = DictionaryProcessor(sample_dict)
    processor.print_large_values()