class ListPrinter:
    SAMPLE_LIST = ['hello', 'world', 'this', 'is', 'Python']

    @staticmethod
    def print_items(items):
        [print(item) for item in items]

if __name__ == '__main__':
    ListPrinter.print_items(ListPrinter.SAMPLE_LIST)