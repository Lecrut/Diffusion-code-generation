class Calculator:
    def __init__(self):
        self.CONSTANT_A = 5
        self.CONSTANT_B = 3

    def add_constants(self):
        return self.CONSTANT_A + self.CONSTANT_B

if __name__ == '__main__':
    calc = Calculator()
    result = calc.add_constants()
    print(result)