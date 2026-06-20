class ArithmeticCalculator:
    NUM1 = 20
    NUM2 = 5

    def __init__(self):
        self.num1 = self.NUM1
        self.num2 = self.NUM2

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
            return "Division by zero error"

if __name__ == '__main__':
    calc = ArithmeticCalculator()
    print("Addition:", calc.add())