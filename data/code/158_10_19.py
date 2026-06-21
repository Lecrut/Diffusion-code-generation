class EvenNumberFinder:
    START = 0
    END = 50

    @staticmethod
    def find_even_numbers(start, end):
        return [num for num in range(start, end + 1) if num % 2 == 0]

if __name__ == '__main__':
    even_finder = EvenNumberFinder()
    print(even_finder.find_even_numbers(EvenNumberFinder.START, EvenNumberFinder.END))