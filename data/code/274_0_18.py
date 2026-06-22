class ListPrinter:
    def __init__(self, items):
        self.items = items

    def print_items(self):
        for item in self.items:
            print(item)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    printer = ListPrinter(sample_list)
    printer.print_items()