class ElementPrinter:
    def __init__(self, elements):
        self.elements = elements

    def print_elements(self):
        for index in range(len(self.elements)):
            try:
                print(self.elements[index])
            except IndexError as e:
                print(f"IndexError: {e}")

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    printer = ElementPrinter(sample_values)
    printer.print_elements()