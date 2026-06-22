class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    x = 10
    y = 25
    calculator = Calculator()
    total = calculator.add(x, y)
    print(total)