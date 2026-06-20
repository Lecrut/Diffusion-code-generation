import operator
MULTIPLY = operator.mul

def compute_product(a, b):
    return MULTIPLY(a, b)
if __name__ == '__main__':
    num1 = 8
    num2 = 3
    product = compute_product(num1, num2)
    print(product)