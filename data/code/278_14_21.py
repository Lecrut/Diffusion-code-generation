class CharacterPrinter:
    def __init__(self, string):
        self.string = string

    def print_chars(self):
        for char in self.string:
            print(char)

if __name__ == '__main__':
    printer = CharacterPrinter("Hello, World!")
    printer.print_chars()