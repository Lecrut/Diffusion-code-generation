class NumberPrinter:
    def print_evens(self):
        for num in range(2, 21, 2):
            print(num)

if __name__ == '__main__':
    printer = NumberPrinter()
    printer.print_evens()