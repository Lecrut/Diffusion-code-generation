class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    calculator = AverageCalculator([42, 35, 28])
    print(calculator.calculate_average())