from decimal import Decimal

class NumericAverageCalculator:
    def __init__(self, values):
        self.values = values
    
    def calculate_average(self):
        if not self.values:
            return Decimal('0')
        
        total = Decimal(0)
        for value in self.values:
            total += Decimal(str(value))
        
        average = total / Decimal(len(self.values))
        return average

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, 8.75]
    calculator = NumericAverageCalculator(sample_values)
    average = calculator.calculate_average()
    print(average)