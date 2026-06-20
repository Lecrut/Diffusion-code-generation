from typing import Union

class BasicArithmetic:
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def divide(a: int, b: int) -> Union[int, float]:
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b

if __name__ == '__main__':
    calculator = BasicArithmetic()
    print(calculator.add(5, 3))
    print(calculator.subtract(10, 4))
    print(calculator.multiply(7, 2))
    try:
        print(calculator.divide(9, 0))
    except ValueError as e:
        print(e)