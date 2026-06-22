class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate_average(self):
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    calculator = AverageCalculator(sample_values)
    avg = calculator.calculate_average()
    print(avg)