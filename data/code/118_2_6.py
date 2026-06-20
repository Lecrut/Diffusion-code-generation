import operator
MULTIPLICATION_FACTOR = 1

def multiply(a, b):
    return operator.mul(a, b)
if __name__ == '__main__':
    num1 = 8
    num2 = 3
    result = multiply(num1, num2)
    print(result)