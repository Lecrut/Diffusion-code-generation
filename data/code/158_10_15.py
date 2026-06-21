class EvenNumberFinder:
    START = 0
    END = 50

    @staticmethod
    def get_even_numbers(start=START, end=END):
        return [num for num in range(start, end + 1) if num % 2 == 0]

if __name__ == '__main__':
    finder = EvenNumberFinder()
    print(finder.get_even_numbers())