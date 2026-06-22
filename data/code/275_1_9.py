class ValueFilter:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def print_large_values(self):
        for key, value in self.dictionary.items():
            if value > 10:
                print(f"{key}: {value}")

if __name__ == '__main__':
    sample_dict = {
        'a': 5,
        'b': 12,
        'c': 8,
        'd': 15
    }
    filter_instance = ValueFilter(sample_dict)
    filter_instance.print_large_values()