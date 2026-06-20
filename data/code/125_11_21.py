class ArithmeticOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

if __name__ == '__main__':
    try:
        op = ArithmeticOperations(10, 5)
        print("Addition result:", op.add())
        print("Subtraction result:", op.subtract())
    except Exception as e:
        print("Error:", str(e))