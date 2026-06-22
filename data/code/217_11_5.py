class MathOperations:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def calculate_addition(self) -> int:
        return self.a + self.b

    def calculate_subtraction(self) -> int:
        return self.a - self.b

    def calculate_multiplication(self) -> int:
        return self.a * self.b

    def calculate_division(self) -> float:
        if self.b == 0:
            raise ValueError("Division by zero is not allowed")
        return self.a / self.b

if __name__ == '__main__':
    math_ops = MathOperations(10, 5)
    print(f"Addition: {math_ops.calculate_addition()}")
    print(f"Subtraction: {math_ops.calculate_subtraction()}")
    print(f"Multiplication: {math_ops.calculate_multiplication()}")
    print(f"Division: {math_ops.calculate_division()}")