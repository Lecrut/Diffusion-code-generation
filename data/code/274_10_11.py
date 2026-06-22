class ListPrinter:
    def print_items(self, lst):
        for item in lst:
            print(item)

if __name__ == '__main__':
    printer = ListPrinter()
    sample_list = ['apple', 'banana', 'cherry']
    printer.print_items(sample_list)