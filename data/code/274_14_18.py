class ItemListPrinter:
    def __init__(self, items):
        self.items = items

    def print_items(self):
        for item in self.items:
            print(item)

if __name__ == '__main__':
    fruit_printer = ItemListPrinter(['apple', 'banana', 'cherry'])
    fruit_printer.print_items()