class ItemPrinter:
    def __init__(self, items):
        self._items = items
    def print_items(self):
        for item in self._items:
            print(item)
if __name__ == '__main__':
    sample_data = ["Apple", "Banana", "Cherry", "Date"]
    printer = ItemPrinter(sample_data)
    printer.print_items()