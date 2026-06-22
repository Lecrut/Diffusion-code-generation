class IntegerPrinter:
    @staticmethod
    def print_integers(integer_list):
        index = 0
        while index < len(integer_list):
            print(integer_list[index])
            index += 1

if __name__ == '__main__':
    sample_values = [7, 8, 9, 10, 11]
    IntegerPrinter.print_integers(sample_values)