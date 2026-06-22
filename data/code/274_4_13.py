class EvenNumberPrinter:
    @staticmethod
    def print_evens(numbers):
        evens = [num for num in numbers if num % 2 == 0]
        for even in evens:
            print(even)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    EvenNumberPrinter.print_evens(sample_list)