class ListPrinter:
    @staticmethod
    def print_items(items):
        for item in items:
            print(item)

if __name__ == '__main__':
    printer = ListPrinter()
    sample_items = ['apple', 'banana', 'cherry']
    printer.print_items(sample_items)