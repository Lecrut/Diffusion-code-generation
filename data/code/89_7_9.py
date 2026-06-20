class ArithmeticOperations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

if __name__ == '__main__':
    print(ArithmeticOperations.add(1.1, 2.2))
    print(ArithmeticOperations.subtract(3.3, 1.1))
    print(ArithmeticOperations.multiply(4.4, 5.5))
    try:
        print(ArithmeticOperations.divide(6.6, 0))
    except ValueError as e:
        print(e)