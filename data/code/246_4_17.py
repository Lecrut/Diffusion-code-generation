class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

if __name__ == '__main__':
    calc = Calculator(15, 27)
    result = calc.add()
    print(result)