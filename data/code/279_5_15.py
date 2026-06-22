class PositiveNumberPrinter:
    def print_positives(self, start, end):
        for number in range(start, end + 1):
            if number > 0:
                print(number)

if __name__ == '__main__':
    printer = PositiveNumberPrinter()
    printer.print_positives(-5, 5)