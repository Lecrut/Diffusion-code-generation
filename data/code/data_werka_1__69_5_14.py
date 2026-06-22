class DataPrinter:
    DEFAULT_DATA = [100, "test", 3.14159, True, None, {'key': 'value'}, [7, 8, 9]]

    @staticmethod
    def print_elements_with_index(elements):
        for index in range(len(elements)):
            element = elements[index]
            print(f"Index: {index}, Element: {element}")

if __name__ == '__main__':
    mixed_data = DataPrinter.DEFAULT_DATA
    DataPrinter.print_elements_with_index(mixed_data)