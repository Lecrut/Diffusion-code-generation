class Calculator:
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

if __name__ == '__main__':
    num1 = 0.1
    num2 = 0.2
    result = Calculator.multiply(num1, num2)
    print(result)