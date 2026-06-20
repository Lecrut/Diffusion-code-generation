class ArithmeticCalculator:
    def __init__(self):
        self.num1 = 10
        self.num2 = 5

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
            raise ValueError("Division by zero error")

if __name__ == '__main__':
    calc = ArithmeticCalculator()
    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
    print("Multiplication:", calc.multiply())
    try:
        print("Division:", calc.divide())
    except ValueError as e:
        print(e)