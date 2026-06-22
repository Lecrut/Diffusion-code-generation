class CharacterPrinter:
    def __init__(self, characters):
        self.characters = characters

    def print_characters(self):
        for char in self.characters:
            ascii_value = ord(char)
            print(f"{char}: {ascii_value}")

if __name__ == '__main__':
    printer = CharacterPrinter("hello")
    printer.print_characters()