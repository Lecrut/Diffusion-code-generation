class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0
    
    @staticmethod
    def calculate_average(total, count):
        return total / count if count > 0 else 0

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values = [1, 2, 3, 4, 5]
    for value in sample_values:
        calculator.count += 1
        calculator.total += value
        print(AverageCalculator.calculate_average(calculator.total, calculator.count))