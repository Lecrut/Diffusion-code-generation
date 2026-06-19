class IncreasingChecker:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_strictly_increasing(self):
        return [self.numbers[i] < self.numbers[i + 1] for i in range(len(self.numbers) - 1)]

if __name__ == '__main__':
    sample_values = [0.5, 1.2, 1.8, 2.3, 3.0]
    checker = IncreasingChecker(sample_values)
    result = checker.is_strictly_increasing()
    print(result)

    another_sample_values = [1.0, 2.5, 3.1, 4.8, 5.0]
    another_checker = IncreasingChecker(another_sample_values)
    another_result = another_checker.is_strictly_increasing()
    print(another_result)