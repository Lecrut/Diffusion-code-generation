class Calculator:
    def multiply(self, a: float, b: float) -> float:
        return a * b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.multiply(3.14159, 2.71828)
    result2 = calc.multiply(4, 3)
    print(result1)
    print(result2)