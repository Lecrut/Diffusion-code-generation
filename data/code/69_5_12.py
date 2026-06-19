class DataPrinter:
    def __init__(self, data):
        self.data = data

    def print_data_with_index(self):
        for index in range(len(self.data)):
            element = self.data[index]
            print(f"Index: {index}, Element: {element}")

if __name__ == '__main__':
    sample_data = [100, "test", 3.14159, True, None, {'key': 'value'}, (1, 2)]
    printer = DataPrinter(sample_data)
    printer.print_data_with_index()