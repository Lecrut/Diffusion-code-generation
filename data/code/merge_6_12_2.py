class Multiplier:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_product(self):
        return self.a * self.b
if __name__ == '__main__':
    m = Multiplier(5, 10)
    result = m.get_product()
    print(result)