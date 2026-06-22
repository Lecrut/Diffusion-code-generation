class AverageCalculator:
    def __init__(self, numbers):
        if not isinstance(numbers, (list, tuple)):
            raise TypeError("Input must be a list or tuple")
        if not numbers:
            raise ValueError("Cannot calculate average of an empty collection")
        self.numbers = numbers

    def compute(self):
        total_value = sum(self.numbers)
        quantity = len(self.numbers)
        return total_value / quantity

if __name__ == '__main__':
    data_points = [15, 25, 35, 45, 55]
    calculator = AverageCalculator(data_points)
    print(calculator.compute())