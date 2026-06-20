class ArithmeticOperations:
    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    result1 = ArithmeticOperations.subtract(10, 5)
    print(f"10 - 5 = {result1}")
    result2 = ArithmeticOperations.subtract(5, 10)
    print(f"5 - 10 = {result2}")
    result3 = ArithmeticOperations.subtract(10, 10)
    print(f"10 - 10 = {result3}")
    result4 = ArithmeticOperations.subtract(-10, 5)
    print(f"-10 - 5 = {result4}")
    result5 = ArithmeticOperations.subtract(5, -10)
    print(f"5 - (-10) = {result5}")
    result6 = ArithmeticOperations.subtract(-10, -5)
    print(f"-10 - (-5) = {result6}")