class CharacterPrinter:
    STRING_TO_PRINT = 'Python'

    @staticmethod
    def print_characters(s):
        for char in s:
            print(char)

if __name__ == '__main__':
    CharacterPrinter.print_characters(CharacterPrinter.STRING_TO_PRINT)