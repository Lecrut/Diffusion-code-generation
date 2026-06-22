class ItemPrinter:
    def __init__(self, items):
        self.items = items

    def print_items_with_index(self):
        for index, item in enumerate(self.items):
            print(f"{index}: {item}")

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    printer = ItemPrinter(sample_list)
    printer.print_items_with_index()