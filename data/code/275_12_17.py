class NestedListPrinter:
    def __init__(self, data):
        self._data = data

    @staticmethod
    def flatten_and_print(data):
        for item in data:
            if isinstance(item, list):
                NestedListPrinter.flatten_and_print(item)
            else:
                print(item)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    printer = NestedListPrinter(sample_data)
    printer.flatten_and_print(sample_data)