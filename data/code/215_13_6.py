class NumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        return max(self.numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 1.9, 5.6]
    finder = NumberFinder(sample_numbers)
    largest_number = finder.find_largest()
    print(largest_number)