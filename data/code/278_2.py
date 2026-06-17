class LinePrinter:
    def print_items(self, items):
        for item in items:
            print(item)
if __name__ == '__main__':
    printer = LinePrinter()
    sample_list = ["Hello", "World", "Python", "OOP"]
    printer.print_items(sample_list)