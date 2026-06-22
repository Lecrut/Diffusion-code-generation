class DictionaryFormatter:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def format_and_print_pairs(self):
        for key, value in self.dictionary.items():
            print(f"Key: {key}, Value: {value}")

if __name__ == '__main__':
    sample_dict = {'x': 10, 'y': 20, 'z': 30}
    formatter = DictionaryFormatter(sample_dict)
    formatter.format_and_print_pairs()