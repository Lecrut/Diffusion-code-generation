class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

if __name__ == '__main__':
    calc = Calculator(10, 5)
    print("Addition Result:", calc.add())
    print("Subtraction Result:", calc.subtract())