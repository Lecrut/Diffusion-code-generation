class Multiplier:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
    def multiply(self, x, y):
        return x * y
if __name__ == '__main__':
    m = Multiplier(5, 10)
    result = m.multiply(3, 4)
    print(result)