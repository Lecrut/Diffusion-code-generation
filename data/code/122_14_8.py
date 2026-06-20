class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_number(self, number):
        self.total += number
        self.count += 1

    def calculate_average(self):
        if self.count == 0:
            return 0.0
        return self.total / self.count

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_numbers = [10, 20, 30, 40, 50]
    for number in sample_numbers:
        calculator.add_number(number)
    print(calculator.calculate_average())