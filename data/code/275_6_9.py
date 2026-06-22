class KeyPrinter:
    def __init__(self, data):
        self.data = data
    
    def print_values(self, key):
        for dictionary in self.data:
            if key in dictionary:
                print(dictionary[key])

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]
    key_to_print = 'name'
    printer = KeyPrinter(sample_dicts)
    printer.print_values(key_to_print)