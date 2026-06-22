class ValuePrinter:
    def __init__(self, dict_list):
        self.dict_list = dict_list

    def print_values_by_key(self, key):
        for dictionary in self.dict_list:
            if key in dictionary:
                print(dictionary[key])

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]
    key_to_print = 'name'
    printer = ValuePrinter(sample_dicts)
    printer.print_values_by_key(key_to_print)