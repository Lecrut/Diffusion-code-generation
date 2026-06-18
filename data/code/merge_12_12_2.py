class ArithmeticLogic:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
if __name__ == '__main__':
    obj = ArithmeticLogic(10, 4)
    print(obj.add())
    print(obj.subtract())