class MixedDataPrinter:
    DATA_TYPES = ["integer", "string", "float", "boolean", "none", "dictionary", "list"]

    @staticmethod
    def get_data_type(element):
        if isinstance(element, int):
            return MixedDataPrinter.DATA_TYPES[0]
        elif isinstance(element, str):
            return MixedDataPrinter.DATA_TYPES[1]
        elif isinstance(element, float):
            return MixedDataPrinter.DATA_TYPES[2]
        elif isinstance(element, bool):
            return MixedDataPrinter.DATA_TYPES[3]
        elif element is None:
            return MixedDataPrinter.DATA_TYPES[4]
        elif isinstance(element, dict):
            return MixedDataPrinter.DATA_TYPES[5]
        elif isinstance(element, list):
            return MixedDataPrinter.DATA_TYPES[6]
        else:
            return "unknown"

    def __init__(self, elements):
        self.elements = elements

    def print_elements_with_index(self):
        for index in range(len(self.elements)):
            element = self.elements[index]
            data_type = MixedDataPrinter.get_data_type(element)
            print(f"Index: {index}, Element: {element} (Type: {data_type})")

if __name__ == '__main__':
    mixed_data = [10, "world", 2.718, False, None, {'a': 'b'}, [4, 5, 6]]
    printer = MixedDataPrinter(mixed_data)
    printer.print_elements_with_index()