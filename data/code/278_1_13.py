class StringPrinter:
    @staticmethod
    def print_separately(strings):
        for index, string in enumerate(strings, start=1):
            print(f"{index}. {string}")

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry"]
    StringPrinter.print_separately(sample_data)