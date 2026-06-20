from decimal import Decimal

class AverageCalculator:
    def __init__(self, values):
        self.values = values

    def calculate_average(self):
        if not self.values:
            return Decimal('0')
        total = sum(Decimal(str(value)) for value in self.values)
        count = Decimal(len(self.values))
        return total / count

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, 8.75]
    calculator = AverageCalculator(sample_values)
    average = calculator.calculate_average()
    print(average)