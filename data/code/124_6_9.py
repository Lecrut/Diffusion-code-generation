class ArithmeticCalculator:
    def __init__(self):
        self.num1 = 7
        self.num2 = 3

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Division by zero"

if __name__ == '__main__':
    calc = ArithmeticCalculator()
    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
    print("Multiplication:", calc.multiply())
    print("Division:", calc.divide())