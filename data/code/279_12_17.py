class EvenNumberPrinter:
    def print_evens(self):
        for num in range(100):
            if num % 2 == 0:
                print(num)

if __name__ == '__main__':
    printer = EvenNumberPrinter()
    printer.print_evens()