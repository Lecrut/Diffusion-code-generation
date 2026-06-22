class ComplexNumberPrinter:
    def __init__(self, numbers):
        self.numbers = numbers

    def print_numbers(self):
        for number in self.numbers:
            print(f"{number.real} + {number.imag}j")

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, 0+5j]
    printer = ComplexNumberPrinter(sample_numbers)
    printer.print_numbers()