class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    calculator = AverageCalculator([10, 20, 30, 40])
    print(calculator.calculate_average())