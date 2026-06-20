class Calculator:
    def multiply(self, a: int, b: int) -> int:
        return a * b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.multiply(4, 3)
    result2 = calc.multiply(-1, -5)
    print(result1, result2)