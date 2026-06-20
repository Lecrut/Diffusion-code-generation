class NumberMultiplier:
    def __init__(self):
        self.pi = 3.141592653589793
        self.e = 2.718281828459045

    def multiply(self):
        return self.pi * self.e

if __name__ == '__main__':
    multiplier = NumberMultiplier()
    result = multiplier.multiply()
    print(result)