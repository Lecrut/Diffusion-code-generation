import statistics

class AverageCalculator:
    def __init__(self):
        self.values = []

    def add_value(self, value):
        self.values.append(value)

    def calculate_average(self):
        if not self.values:
            return None
        return statistics.mean(self.values)

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add_value(10)
    calculator.add_value(25)
    calculator.add_value(32)
    calculator.add_value(48)
    calculator.add_value(15)
    print(calculator.calculate_average())