class IntegerPrinter:
    def print_integers(self, integer_list):
        index = 0
        while index < len(integer_list):
            print(integer_list[index])
            index += 1

if __name__ == '__main__':
    printer = IntegerPrinter()
    sample_values = [15, 25, 35, 45, 55]
    printer.print_integers(sample_values)