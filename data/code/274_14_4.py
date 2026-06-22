class ItemPrinter:
    def __init__(self, items):
        self.items = items

    def print_items(self):
        for item in self.items:
            print(item)

if __name__ == '__main__':
    printer = ItemPrinter(['apple', 'banana', 'cherry'])
    printer.print_items()