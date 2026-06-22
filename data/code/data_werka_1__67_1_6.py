class Calculator:
    def __init__(self):
        self.DEFAULT_VALUE = 0

    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result = calc.add(7, 13)
    print(result)