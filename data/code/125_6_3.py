class Calculator:
    def add(self, a: int, b: int) -> int:
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both inputs must be integers.")
        return a + b

    def subtract(self, a: int, b: int) -> int:
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both inputs must be integers.")
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(10, 5))
    print(calc.subtract(20, 8))