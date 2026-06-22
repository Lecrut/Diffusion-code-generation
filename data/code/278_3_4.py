class StringPrinter:
    def print_strings_with_exclamation(self, strings):
        for s in strings:
            print(f"{s}!")

if __name__ == '__main__':
    printer = StringPrinter()
    sample_values = ("Hello", "World", "Python")
    printer.print_strings_with_exclamation(sample_values)