class FloatingPointCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate_difference(self):
        return round(self.num1 - self.num2, 4)

if __name__ == '__main__':
    calculator = FloatingPointCalculator(15.0, 7.0)
    result = calculator.calculate_difference()
    print(result)