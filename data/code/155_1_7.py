from functools import reduce

class SumCalculator:
    def __init__(self):
        self.samples = [1, 2, 3, 4, 5], (10, 20, 30), [], [42]

    def compute_sum(self, iterable):
        return reduce(lambda x, y: x + y, iterable)

if __name__ == '__main__':
    calculator = SumCalculator()
    for sample in calculator.samples:
        print(f"Sum of {sample}: {calculator.compute_sum(sample)}")