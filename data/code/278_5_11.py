class AsciiPrinter:
    @staticmethod
    def print_ascii(characters):
        for char in characters:
            print(f"{char}: {ord(char)}")

if __name__ == '__main__':
    sample_chars = "Hello, World!"
    AsciiPrinter.print_ascii(sample_chars)