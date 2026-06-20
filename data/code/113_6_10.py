class Calculator:
    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.subtract(100, 45)
    print(f"Result of 100 - 45: {result1}")
    result2 = calc.subtract(50, 150)
    print(f"Result of 50 - 150: {result2}")