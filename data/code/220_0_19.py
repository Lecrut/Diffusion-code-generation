import statistics

class AverageCalculator:
    def __init__(self):
        self.values = []

    def add_value(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        self.values.append(value)

    def calculate_average(self) -> float:
        if not self.values:
            raise ValueError("Cannot compute average of an empty list")
        return statistics.mean(self.values)

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add_value(3.5)
    calculator.add_value(4.0)
    calculator.add_value(2.5)
    print(calculator.calculate_average())