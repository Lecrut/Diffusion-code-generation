class EvenNumberPrinter:
    START = 1
    END = 20
    STEP = 2

    @staticmethod
    def print_evens(start, end, step):
        for num in range(start, end + 1, step):
            print(num)

if __name__ == '__main__':
    printer = EvenNumberPrinter()
    printer.print_evens(EvenNumberPrinter.START, EvenNumberPrinter.END, EvenNumberPrinter.STEP)