class SimpleArithmetic:
    def __init__(self, num1: int, num2: int):
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Both inputs must be integers")
        self.num1 = num1
        self.num2 = num2

    def add(self) -> int:
        return self.num1 + self.num2

    def subtract(self) -> int:
        return self.num1 - self.num2

if __name__ == '__main__':
    calc = SimpleArithmetic(5, 3)
    print("Addition result:", calc.add())
    print("Subtraction result:", calc.subtract())