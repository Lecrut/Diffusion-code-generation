class EvenNumberFinder:
    def find_evens(self, start, end):
        return [num for num in range(start, end + 1) if num % 2 == 0]

if __name__ == '__main__':
    finder = EvenNumberFinder()
    evens = finder.find_evens(0, 99)
    print(evens)