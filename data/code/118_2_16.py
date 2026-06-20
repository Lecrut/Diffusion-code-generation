import operator

def multiply(a, b):
    return operator.mul(a, b)

if __name__ == '__main__':
    num1 = 3
    num2 = 9
    result = multiply(num1, num2)
    print(result)