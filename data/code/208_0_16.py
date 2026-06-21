import statistics

class MeanCalculator:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def calculate_mean(self):
        if not self.numbers:
            return 0
        return statistics.mean(self.numbers)

if __name__ == '__main__':
    calculator = MeanCalculator()
    calculator.add_number(3.5)
    calculator.add_number(2.1)
    calculator.add_number(4.8)
    calculator.add_number(6.7)
    calculator.add_number(5.0)
    print(calculator.calculate_mean())