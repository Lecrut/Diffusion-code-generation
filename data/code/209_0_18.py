import statistics

class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate_average(self):
        return statistics.mean(self.numbers)

if __name__ == '__main__':
    calculator = AverageCalculator([10, 20, 30, 40, 50])
    avg_result = calculator.calculate_average()
    print(avg_result)