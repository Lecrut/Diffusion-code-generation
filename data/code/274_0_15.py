class ListPrinter:
    SAMPLE_LIST = ["apple", "banana", "cherry", "date"]

    @staticmethod
    def print_items(items):
        for item in items:
            print(item)

if __name__ == '__main__':
    printer = ListPrinter()
    printer.print_items(ListPrinter.SAMPLE_LIST)