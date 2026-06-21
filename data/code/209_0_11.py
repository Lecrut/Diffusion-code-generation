import statistics

class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate(self):
        return statistics.mean(self.numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    calculator = AverageCalculator(sample_values)
    average = calculator.calculate()
    print(average)