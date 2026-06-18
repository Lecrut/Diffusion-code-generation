class ArithmeticLogic:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
if __name__ == '__main__':
    obj = ArithmeticLogic(10, 4)
    print(obj.add())
    print(obj.subtract())