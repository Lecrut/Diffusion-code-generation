class DataPrinter:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list.")
        self.data = data

    def print_data(self):
        for index in range(len(self.data)):
            element = self.data[index]
            print(f"Index: {index}, Element: {element}")

if __name__ == '__main__':
    mixed_data = [10, "hello", 3.14, True, None, {'key': 'value'}, (1, 2, 3)]
    printer = DataPrinter(mixed_data)
    printer.print_data()