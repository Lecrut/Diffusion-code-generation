class DataPrinter:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list.")
        self.data = data

    def print_data_with_index(self):
        for index in range(len(self.data)):
            try:
                element = self.data[index]
                print(f"Index: {index}, Element: {element}")
            except Exception as e:
                print(f"Error accessing element at index {index}: {e}")

if __name__ == '__main__':
    mixed_data = [42, "hello", 3.14, True, None, {'key': 'value'}, [1, 2, 3], 7+8j, b"bytes"]
    printer = DataPrinter(mixed_data)
    printer.print_data_with_index()