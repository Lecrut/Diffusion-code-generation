class Calculator:
    def subtract(self, a: float, b: float) -> float:
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.subtract(10.5, 3.2)
    print(result1)
    result2 = calc.subtract(7, 4)
    print(result2)