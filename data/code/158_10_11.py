class EvenNumberFinder:
    def find_evens(self, start=0, end=50):
        return [num for num in range(start, end + 1) if num % 2 == 0]

if __name__ == '__main__':
    finder = EvenNumberFinder()
    even_numbers = finder.find_evens()
    print(even_numbers)