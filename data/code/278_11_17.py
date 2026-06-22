class ItemPrinter:
    @staticmethod
    def print_items_separately(items):
        for item in items:
            print(item)

if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    data2 = ('a', 'b', 'c', 'd')
    data3 = [10.5, 20.1, 33.9]

    ItemPrinter.print_items_separately(data1)
    ItemPrinter.print_items_separately(data2)
    ItemPrinter.print_items_separately(data3)