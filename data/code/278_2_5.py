class IntegerPrinter:
    def print_numbers(self, numbers):
        index = 0
        while index < len(numbers):
            print(numbers[index])
            index += 1

if __name__ == '__main__':
    printer = IntegerPrinter()
    sample_values = [1, 2, 3, 4, 5]
    printer.print_numbers(sample_values)