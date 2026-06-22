class DictFormatter:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def format_and_print(self):
        for key, value in self.dictionary.items():
            print(f"Key: {key}, Value: {value}")

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    formatter = DictFormatter(sample_dict)
    formatter.format_and_print()