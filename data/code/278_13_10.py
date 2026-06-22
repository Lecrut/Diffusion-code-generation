class IntegerPrinter:
    @staticmethod
    def print_numbers(number_list):
        for number in number_list:
            print(number)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    IntegerPrinter.print_numbers(sample_values)