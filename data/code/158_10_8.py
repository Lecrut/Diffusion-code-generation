class NumberFinder:
    def find_even_numbers(self, start, end):
        return [num for num in range(start, end + 1) if num % 2 == 0]

if __name__ == '__main__':
    finder = NumberFinder()
    even_numbers = finder.find_even_numbers(0, 50)
    print(even_numbers)