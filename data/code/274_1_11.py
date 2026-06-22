class ListPrinter:
    @staticmethod
    def print_items(iterable):
        for item in iterable:
            print(item)

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    ListPrinter.print_items(sample_list)
    sample_tuple = ('a', 'b', 'c')
    ListPrinter.print_items(sample_tuple)