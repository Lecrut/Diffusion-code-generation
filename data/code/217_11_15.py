class MathOperations:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def calculate_operations(self) -> dict:
        return {
            'addition': self.a + self.b,
            'subtraction': self.a - self.b,
            'multiplication': self.a * self.b,
            'division': self.a / self.b if self.b != 0 else None
        }

if __name__ == '__main__':
    math_ops1 = MathOperations(10, 5)
    result1 = math_ops1.calculate_operations()
    print(f"Operations for (10, 5): {result1}")

    math_ops2 = MathOperations(7, 7)
    result2 = math_ops2.calculate_operations()
    print(f"Operations for (7, 7): {result2}")