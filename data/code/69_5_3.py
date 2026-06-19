class ElementPrinter:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Input must be a list.")
        self.elements = elements

    def print_elements(self):
        for index in range(len(self.elements)):
            element = self.elements[index]
            print(f"Index: {index}, Element: {element}")

if __name__ == '__main__':
    mixed_data = [7, "example", 2.0, False, None, {'x': 'y'}, (7, 8, 9)]
    printer = ElementPrinter(mixed_data)
    printer.print_elements()