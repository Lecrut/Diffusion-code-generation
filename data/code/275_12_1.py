class DictionaryPrinter:
    def __init__(self, data):
        self._data = data
    def print_dictionary(self):
        for key, value in self._data.items():
            print(f"Key: {key}, Value: {value}")
if __name__ == '__main__':
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    printer = DictionaryPrinter(sample_data)
    printer.print_dictionary()