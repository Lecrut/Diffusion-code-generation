from functools import mul

class Multiplier:
    def multiply(self, a, b):
        return mul(a, b)

if __name__ == '__main__':
    multiplier = Multiplier()
    result1 = multiplier.multiply(4, 3)
    result2 = multiplier.multiply(7, 2)
    print(result1)
    print(result2)