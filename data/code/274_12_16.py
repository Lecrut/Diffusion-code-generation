class ItemPrinter:
    def __init__(self, items):
        self.items = items

    def print_items(self):
        [print(item) for item in self.items]

if __name__ == '__main__':
    printer = ItemPrinter(['apple', 'banana', 'cherry'])
    printer.print_items()