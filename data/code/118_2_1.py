import operator

def multiply(a, b):
    return operator.mul(a, b)

if __name__ == '__main__':
    result = multiply(4, 5)
    print(result)