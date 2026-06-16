class ListPrinter:
    def print_list(self, data):
        for item in data:
            print(item)
if __name__ == '__main__':
    my_list = [1, "hello", 3.14, True]
    printer = ListPrinter()
    printer.print_list(my_list)