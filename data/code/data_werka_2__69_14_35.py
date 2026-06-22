class ElementPrinter:
    def __init__(self, elements):
        self.elements = elements

    def print_elements(self):
        for index in range(len(self.elements)):
            print(self.elements[index])

    def count_elements(self):
        return len(self.elements)

if __name__ == '__main__':
    sample_values = [10000, 20000, 30000, 40000, 50000]
    printer = ElementPrinter(sample_values)
    printer.print_elements()
    print("Total elements:", printer.count_elements())