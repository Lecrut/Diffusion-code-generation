class ListPrinter:
    def print_items(self, iterable):
        for item in iterable:
            print(item)

if __name__ == '__main__':
    printer = ListPrinter()
    sample_list = [1, "hello", 3.14, True]
    printer.print_items(sample_list)
    
    sample_tuple = ('a', 'b', 'c')
    printer.print_items(sample_tuple)