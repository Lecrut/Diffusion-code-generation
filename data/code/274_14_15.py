class ItemPrinter:
    DEFAULT_ITEMS = ['apple', 'banana', 'cherry']

    @staticmethod
    def print_items(item_list):
        for item in item_list:
            print(item)

if __name__ == '__main__':
    printer = ItemPrinter()
    printer.print_items(ItemPrinter.DEFAULT_ITEMS)