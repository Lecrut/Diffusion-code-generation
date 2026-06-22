class DictPrinter:
    HEADER = "Key: {key}, Value: {value}"

    @staticmethod
    def print_pairs(dictionary):
        for key, value in dictionary.items():
            print(DictPrinter.HEADER.format(key=key, value=value))

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    DictPrinter.print_pairs(sample_dict)