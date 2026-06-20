class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.subtract(10, 4))