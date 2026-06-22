class StringPrinter:
    def print_items(self, iterable):
        for item in iterable:
            print(item)

if __name__ == '__main__':
    printer = StringPrinter()
    data1 = ('Hello', 'World')
    printer.print_items(data1)
    data2 = ('Python', 'is', 'awesome!')
    printer.print_items(data2)