class ListPrinter:
    SAMPLE_LIST = [1, 2, 3, 4, 5]

    @staticmethod
    def print_items():
        [print(item) for item in ListPrinter.SAMPLE_LIST]

if __name__ == '__main__':
    ListPrinter.print_items()