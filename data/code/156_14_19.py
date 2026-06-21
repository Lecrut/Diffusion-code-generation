import math

class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_number(self, number):
        self.total += number
        self.count += 1

    def calculate_average(self):
        if self.count == 0:
            return 0
        return math.fsum([self.total / self.count])

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add_number(1)
    calculator.add_number(2)
    calculator.add_number(3)
    print(f"Average: {calculator.calculate_average()}")

    calculator = AverageCalculator()
    calculator.add_number(10)
    calculator.add_number(20)
    calculator.add_number(30)
    calculator.add_number(40)
    calculator.add_number(50)
    calculator.add_number(60)
    print(f"Average: {calculator.calculate_average()}")

    calculator = AverageCalculator()
    print(f"Average: {calculator.calculate_average()}")

    calculator = AverageCalculator()
    calculator.add_number(1.5)
    calculator.add_number(2.5)
    calculator.add_number(3.5)
    print(f"Average: {calculator.calculate_average()}")