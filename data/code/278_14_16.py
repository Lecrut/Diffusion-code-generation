class StringCharacterPrinter:
    STRING_TO_PRINT = "Hello, World!"
    
    @staticmethod
    def print_chars():
        for char in StringCharacterPrinter.STRING_TO_PRINT:
            print(char)

if __name__ == '__main__':
    StringCharacterPrinter.print_chars()