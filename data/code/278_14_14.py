class StringCharacterPrinter:
    DEFAULT_STRING = "Hello, World!"

    @staticmethod
    def print_chars(input_string=DEFAULT_STRING):
        for char in input_string:
            print(char)

if __name__ == '__main__':
    printer = StringCharacterPrinter()
    printer.print_chars()