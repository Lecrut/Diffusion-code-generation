class ArithmeticOperations:
    @staticmethod
    def calculate_difference(a: int, b: int) -> int:
        return a - b

if __name__ == '__main__':
    num1 = 25
    num2 = 10
    result = ArithmeticOperations.calculate_difference(num1, num2)
    print(result)