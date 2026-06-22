class StringPrinter:
    DEFAULT_STRING = "Hello, World!"

    @staticmethod
    def print_chars(input_string=DEFAULT_STRING):
        for char in input_string:
            print(char)

if __name__ == '__main__':
    printer = StringPrinter()
    printer.print_chars()