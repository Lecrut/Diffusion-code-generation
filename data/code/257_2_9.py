class AbsoluteDifferenceCalculator:
    @staticmethod
    def calculate_abs_diff(a, b):
        return ((a - b) ^ (a - b >> 31)) & 0xFFFFFFFF

if __name__ == '__main__':
    calculator = AbsoluteDifferenceCalculator()
    num1 = 10
    num2 = 5
    result = calculator.calculate_abs_diff(num1, num2)
    print(result)