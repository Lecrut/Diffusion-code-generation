class StringPrinter:
    def print_strings(self, strings):
        for s in strings:
            print(s)

if __name__ == '__main__':
    printer = StringPrinter()
    sample_tuple = ('Hello', 'World', 'This', 'Is', 'A', 'Test')
    printer.print_strings(sample_tuple)