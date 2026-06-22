class IntegerPrinter:
    def __init__(self, integers):
        self._integers = integers

    def print_integers(self):
        for number in self._integers:
            print(number)

if __name__ == '__main__':
    sample_integers = [10, 20, 30, 40, 50]
    printer = IntegerPrinter(sample_integers)
    printer.print_integers()