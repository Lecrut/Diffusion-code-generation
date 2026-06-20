import operator

def multiply(a, b):
    return operator.mul(a, b)

if __name__ == '__main__':
    value1 = 8
    value2 = 3
    product = multiply(value1, value2)
    print(product)