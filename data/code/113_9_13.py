class Calculator:
    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.subtract(10, 5)
    result2 = calc.subtract(100, 30)
    print(result1)
    print(result2)