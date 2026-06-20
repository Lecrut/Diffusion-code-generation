class MathOperations:
    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    calculator = MathOperations()
    result1 = calculator.subtract(10, 5)
    print(f"10 - 5 = {result1}")
    result2 = calculator.subtract(5, 10)
    print(f"5 - 10 = {result2}")
    result3 = calculator.subtract(10, 10)
    print(f"10 - 10 = {result3}")
    result4 = calculator.subtract(-10, 5)
    print(f"-10 - 5 = {result4}")
    result5 = calculator.subtract(5, -10)
    print(f"5 - (-10) = {result5}")
    result6 = calculator.subtract(-10, -5)
    print(f"-10 - (-5) = {result6}")