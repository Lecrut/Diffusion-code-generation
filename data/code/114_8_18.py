class Multiplier:
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    multiplier = Multiplier()
    print(multiplier.multiply(2, 3))
    print(multiplier.multiply(-4, -5))
    print(multiplier.multiply(0, 10))