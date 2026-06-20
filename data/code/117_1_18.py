class DifferenceCalculator:
    @staticmethod
    def calculate_difference(a, b):
        return abs(a - b)

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    num1 = 10
    num2 = 4
    result1 = calculator.calculate_difference(num1, num2)
    print(result1)
    num3 = 35
    num4 = 7
    result2 = calculator.calculate_difference(num3, num4)
    print(result2)