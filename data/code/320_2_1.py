class Subtractor:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def subtract(self):
        return self.a - self.b
if __name__ == '__main__':
    num1 = 20
    num2 = 7
    sub = Subtractor(num1, num2)
    result = sub.subtract()
    print(result)