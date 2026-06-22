class ListPrinter:
    def __init__(self, items):
        self.items = items

    def print_items(self):
        for item in self.items:
            print(item)

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    printer = ListPrinter(sample_items)
    printer.print_items()