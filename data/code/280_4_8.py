class SquarePrinter:
    def print_squares(self):
        for i in range(1, 21):
            print(i ** 2)

if __name__ == '__main__':
    printer = SquarePrinter()
    printer.print_squares()