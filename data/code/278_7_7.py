class UnicodePrinter:
    def print_unicode(self, string):
        for char in string:
            print(f"'{char}': {ord(char)}")

if __name__ == '__main__':
    printer = UnicodePrinter()
    sample_string = "hello"
    printer.print_unicode(sample_string)