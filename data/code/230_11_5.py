class UppercasePrinter:
    def print_uppercase_pairs(self, dictionary):
        for key, value in dictionary.items():
            print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    printer = UppercasePrinter()
    sample_dict = {
        'apple': 'fruit',
        'carrot': 'vegetable',
        'banana': 'fruit'
    }
    printer.print_uppercase_pairs(sample_dict)