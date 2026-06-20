class Calculator:
    def subtract(self, value1, value2):
        return value1 - value2

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.subtract(10, 5)
    result2 = calc.subtract(7, 3)
    print(f"Result of subtraction (10 - 5): {result1}")
    print(f"Result of subtraction (7 - 3): {result2}")