class Multiplier:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def multiply(self, x, y):
        return x * y
if __name__ == '__main__':
    m = Multiplier(5, 10)
    result1 = m.multiply(3, 4)
    print(f"Result of multiplying 3 and 4: {result1}")
    m2 = Multiplier()
    result2 = m2.multiply(7, 8)
    print(f"Result of multiplying 7 and 8: {result2}")