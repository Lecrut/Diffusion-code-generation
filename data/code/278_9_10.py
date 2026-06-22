class ComplexNumberPrinter:
    def print_numbers(self, numbers):
        for number in numbers:
            print(f"{number.real} + {number.imag}j")

if __name__ == '__main__':
    printer = ComplexNumberPrinter()
    sample_numbers = [3+4j, 1-2j, 0+5j]
    printer.print_numbers(sample_numbers)