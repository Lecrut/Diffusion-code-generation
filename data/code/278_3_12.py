class StringPrinter:
    def print_strings_with_exclamation(self, strings):
        for string in strings:
            print(f"{string}!")

if __name__ == '__main__':
    printer = StringPrinter()
    sample_values = ("Hello", "World", "Python")
    printer.print_strings_with_exclamation(sample_values)