class UnicodePrinter:
    @staticmethod
    def print_char_unicode(char):
        print(f'{char}: {ord(char)}')

if __name__ == '__main__':
    sample_string = "hello"
    for char in sample_string:
        UnicodePrinter.print_char_unicode(char)