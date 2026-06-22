class IntegerPrinter:
    def __init__(self, integers):
        self._integers = integers

    def print_integers(self):
        for integer in self._integers:
            print(integer)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    printer = IntegerPrinter(sample_values)
    printer.print_integers()