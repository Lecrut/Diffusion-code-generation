class StringPrinter:
    EXCLAMATION = '!'

    @staticmethod
    def print_strings_with_exclamation(strings):
        for s in strings:
            print(f"{s}{StringPrinter.EXCLAMATION}")

if __name__ == '__main__':
    sample_values = ("Hello", "World", "Python")
    StringPrinter.print_strings_with_exclamation(sample_values)