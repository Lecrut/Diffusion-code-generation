from statistics import mean

class AverageCalculator:
    def __init__(self):
        self.values = []

    def add_value(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        self.values.append(value)

    def calculate_average(self) -> float:
        if len(self.values) == 0:
            raise ValueError("No values to average")
        return mean(self.values)

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add_value(1.5)
    calculator.add_value(2.5)
    calculator.add_value(3.5)
    print(calculator.calculate_average())