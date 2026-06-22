class ListPrinter:
    def __init__(self, items):
        self.items = items

    @staticmethod
    def print_items(items):
        for item in items:
            print(item)

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    list_printer = ListPrinter(sample_items)
    ListPrinter.print_items(list_printer.items)