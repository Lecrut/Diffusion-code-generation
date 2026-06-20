from functools import mul
MULTIPLICATION_CONSTANT = 2

def multiply(a, b):
    return mul(a, b)
if __name__ == '__main__':
    sample_a = 5
    sample_b = 3
    product = multiply(sample_a, MULTIPLICATION_CONSTANT)
    print(product)