class DictPrinter:
    @staticmethod
    def print_pairs(dictionary):
        for key, value in dictionary.items():
            print(f'Key: {key}, Value: {value}')

if __name__ == '__main__':
    sample_dict = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
    DictPrinter.print_pairs(sample_dict)