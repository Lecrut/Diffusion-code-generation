class ComplexNumberPrinter:
    def __init__(self, numbers):
        self.numbers = numbers

    @staticmethod
    def format_complex_number(number):
        return f"{number.real} + {number.imag}j"

    def print_numbers(self):
        for number in self.numbers:
            print(self.format_complex_number(number))

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, 0+5j]
    printer = ComplexNumberPrinter(sample_numbers)
    printer.print_numbers()