class OddNumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_odd(self, num):
        return num & 1

    def find_odd_numbers(self):
        return [num for num in self.numbers if self.is_odd(num)]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    finder = OddNumberFinder(sample_values)
    print(finder.find_odd_numbers())