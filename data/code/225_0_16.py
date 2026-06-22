class MinMaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_min_max(self):
        if not self.numbers:
            raise ValueError("The list of numbers is empty")
        minimum = min(self.numbers)
        maximum = max(self.numbers)
        return minimum, maximum

if __name__ == '__main__':
    sample_numbers = [15, 3, 8, 22, 1, 45]
    finder = MinMaxFinder(sample_numbers)
    min_val, max_val = finder.find_min_max()
    print(f"The list of numbers is: {sample_numbers}")
    print(f"The minimum value is: {min_val}")
    print(f"The maximum value is: {max_val}")