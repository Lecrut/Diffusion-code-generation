class CharacterPrinter:
    @staticmethod
    def print_characters(s):
        for char in s:
            print(char)

if __name__ == '__main__':
    printer = CharacterPrinter()
    printer.print_characters('Python')