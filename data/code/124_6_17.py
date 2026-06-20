class ArithmeticCalculator:
    def __init__(self):
        self.NUM1 = 8
        self.NUM2 = 4

    def add(self):
        return self.NUM1 + self.NUM2

    def subtract(self):
        return self.NUM1 - self.NUM2

    def multiply(self):
        return self.NUM1 * self.NUM2

    def divide(self):
        if self.NUM2 != 0:
            return self.NUM1 / self.NUM2
        else:
            return "Division by zero error"

if __name__ == '__main__':
    calc = ArithmeticCalculator()
    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
    print("Multiplication:", calc.multiply())
    print("Division:", calc.divide())