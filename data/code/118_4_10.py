from functools import mul

class MathOperations:
    @staticmethod
    def multiply(a, b):
        return mul(a, b)

if __name__ == '__main__':
    result = MathOperations.multiply(4, 3)
    print(result)