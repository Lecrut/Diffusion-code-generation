from functools import mul

class MathOperations:
    @staticmethod
    def multiply(a, b):
        return mul(a, b)

if __name__ == '__main__':
    sample_a = 8
    sample_b = 3
    product = MathOperations.multiply(sample_a, sample_b)
    print(product)