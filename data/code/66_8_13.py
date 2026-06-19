class AdjacentPairChecker:
    def __init__(self, numbers):
        self.numbers = numbers

    def compare_adjacent(self):
        return [self.numbers[i] < self.numbers[i + 1] for i in range(len(self.numbers) - 1)]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    checker = AdjacentPairChecker(sample_values)
    result = checker.compare_adjacent()
    print(result)