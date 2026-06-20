from typing import Tuple

class ArithmeticCalculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self) -> int:
        return self.a + self.b

    def subtract(self) -> int:
        return self.a - self.b

    def multiply(self) -> int:
        return self.a * self.b

    def divide(self) -> float:
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

if __name__ == '__main__':
    calc = ArithmeticCalculator(100, 7)
    print(f"Addition: {calc.add()}")
    print(f"Subtraction: {calc.subtract()}")
    print(f"Multiplication: {calc.multiply()}")
    print(f"Division: {calc.divide()}")