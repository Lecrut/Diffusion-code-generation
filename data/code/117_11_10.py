class AbsoluteDifferenceCalculator:
    def calculate_difference(self, a, b):
        return abs(a - b)

if __name__ == '__main__':
    calculator = AbsoluteDifferenceCalculator()
    print(calculator.calculate_difference(10, 5))
    print(calculator.calculate_difference(-3, -7))
    print(calculator.calculate_difference(0, 0))