import operator

def multiply(x, y):
    return operator.mul(x, y)

if __name__ == '__main__':
    result = multiply(3, 4)
    print(result)