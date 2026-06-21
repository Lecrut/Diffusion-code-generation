class EvenNumberPrinter:
    START = 1
    END = 20
    STEP = 2

    @staticmethod
    def print_evens():
        for num in range(EvenNumberPrinter.START, EvenNumberPrinter.END + 1, EvenNumberPrinter.STEP):
            print(num)

if __name__ == '__main__':
    printer = EvenNumberPrinter()
    printer.print_evens()