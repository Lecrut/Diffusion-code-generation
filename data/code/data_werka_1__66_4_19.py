class IncreasingChecker:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_strictly_increasing(self):
        return [self.numbers[i] < self.numbers[i + 1] for i in range(len(self.numbers) - 1)]

if __name__ == '__main__':
    sample_values = [3.5, 4.2, 5.0, 6.8, 7.1]
    checker = IncreasingChecker(sample_values)
    result = checker.is_strictly_increasing()
    print(result)

    another_sample = [1.1, 1.1, 2.2, 3.3, 4.4]
    another_checker = IncreasingChecker(another_sample)
    another_result = another_checker.is_strictly_increasing()
    print(another_result)