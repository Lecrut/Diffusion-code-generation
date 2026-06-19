class DataPrinter:
    def __init__(self, data):
        self.data = data

    def print_with_index(self):
        for index in range(len(self.data)):
            element = self.data[index]
            print(f"Index: {index}, Element: {element}")

if __name__ == '__main__':
    mixed_data = [42, "hello", 3.14, True, None, {'key': 'value'}, [1, 2, 3]]
    printer = DataPrinter(mixed_data)
    printer.print_with_index()