class AverageCalculator:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def get_average(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add_number(10)
    calculator.add_number(20)
    calculator.add_number(30)
    print(calculator.get_average())