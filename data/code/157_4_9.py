class NumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def validate_numbers(self):
        if not all(isinstance(n, (int, float)) for n in self.numbers):
            raise ValueError("All elements in the list must be numeric")

    def find_smallest_value(self):
        self.validate_numbers()
        return min(self.numbers)

if __name__ == '__main__':
    sample_values = [-5, 3, -1, 2, -4]
    finder = NumberFinder(sample_values)
    print(finder.find_smallest_value())