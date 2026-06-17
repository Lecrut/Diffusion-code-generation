class Multiplier:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def multiply(self):
        return self.a * self.b
if __name__ == '__main__':
    m = Multiplier(5, 10)
    result = m.multiply()
    print(result)