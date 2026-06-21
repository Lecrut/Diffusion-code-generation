class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    calculator = AverageCalculator([1.0, 2.0, 3.0, 4.0, 5.0])
    print(calculator.calculate_average())