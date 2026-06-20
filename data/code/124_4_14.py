class Calculator:
    def __init__(self):
        self.add = lambda x, y: x + y
        self.sub = lambda x, y: x - y
        self.mul = lambda x, y: x * y
        self.div = lambda x, y: x / y if y != 0 else "Error: Division by zero"

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(8, 2))
    print(calc.sub(8, 2))
    print(calc.mul(8, 2))
    print(calc.div(8, 2))