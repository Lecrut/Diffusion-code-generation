class DictPrinter:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def print_pairs(self):
        for key, value in self.dictionary.items():
            print(f'{key}: {value}')

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    printer = DictPrinter(sample_dict)
    printer.print_pairs()