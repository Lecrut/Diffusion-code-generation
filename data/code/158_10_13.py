class EvenNumberFinder:
    START = 0
    END = 50

    @staticmethod
    def find_evens(start=START, end=END):
        return [num for num in range(start, end + 1) if num % 2 == 0]

if __name__ == '__main__':
    even_numbers = EvenNumberFinder.find_evens()
    print(even_numbers)