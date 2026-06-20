import operator

def compute_product(a, b):
    return operator.mul(a, b)

if __name__ == '__main__':
    num1 = 7
    num2 = 6
    product = compute_product(num1, num2)
    print(product)