class BasicMathOperations:
    ADD = "add"
    SUBTRACT = "subtract"

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b

if __name__ == '__main__':
    calc = BasicMathOperations()
    print(calc.add(10, 5))
    print(calc.subtract(20, 8))