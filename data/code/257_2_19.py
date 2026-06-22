class AbsoluteDifferenceCalculator:
    @staticmethod
    def calculate_difference(a, b):
        return ((a - b) ^ (a - b >> 31)) & ((a - b + 1) >> 31)

if __name__ == '__main__':
    calculator = AbsoluteDifferenceCalculator()
    num1 = 10
    num2 = 5
    result = calculator.calculate_difference(num1, num2)
    print(result)