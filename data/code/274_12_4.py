class ItemPrinter:
    SAMPLE_ITEMS = ['apple', 'banana', 'cherry']

    @staticmethod
    def print_items(items):
        [print(item) for item in items]

if __name__ == '__main__':
    ItemPrinter.print_items(ItemPrinter.SAMPLE_ITEMS)