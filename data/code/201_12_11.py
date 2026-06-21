class MeanCalculator:
    def __init__(self, numbers):
        if not all(isinstance(num, float) for num in numbers):
            raise TypeError("All elements in the iterable must be floats")
        self.total = sum(numbers)
        self.count = len(numbers)

    def calculate_mean(self):
        return self.total / self.count

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    calculator = MeanCalculator(sample_values)
    print(calculator.calculate_mean())