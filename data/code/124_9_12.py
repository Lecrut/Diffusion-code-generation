class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

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
            raise ValueError("Undefined (Division by zero)")

if __name__ == '__main__':
    calc = Calculator(20, 4)
    print(f"Sum: {calc.add()}")
    print(f"Difference: {calc.subtract()}")
    print(f"Product: {calc.multiply()}")
    try:
        print(f"Quotient: {calc.divide()}")
    except ValueError as e:
        print(e)