class ArithmeticOperations:
    @staticmethod
    def calculate_difference(value1: float, value2: float) -> float:
        return value1 - value2

if __name__ == '__main__':
    try:
        num1 = 100.5
        num2 = 45.2
        result = ArithmeticOperations.calculate_difference(num1, num2)
        print(result)
    except TypeError as e:
        print(e)