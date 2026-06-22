class StringPrinter:
    @staticmethod
    def print_with_exclamation(strings):
        for s in strings:
            print(f"{s}!")

if __name__ == '__main__':
    sample_values = ("Hello", "World", "Python")
    StringPrinter.print_with_exclamation(sample_values)