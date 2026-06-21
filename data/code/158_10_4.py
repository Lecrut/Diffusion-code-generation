class EvenNumberFinder:
    START = 0
    END = 50

    @staticmethod
    def find_even_numbers():
        return [num for num in range(EvenNumberFinder.START, EvenNumberFinder.END + 1) if num % 2 == 0]

if __name__ == '__main__':
    even_numbers = EvenNumberFinder.find_even_numbers()
    print(even_numbers)