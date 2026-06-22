class StringPrinter:
    def print_separately(self, strings):
        for index, string in enumerate(strings, start=1):
            print(f"{index}. {string}")

if __name__ == '__main__':
    printer = StringPrinter()
    sample_strings = ["apple", "banana", "cherry"]
    printer.print_separately(sample_strings)