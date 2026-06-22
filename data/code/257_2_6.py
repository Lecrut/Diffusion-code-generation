ABSOLUTE_ZERO = 0

def abs_diff(a, b):
    return ((a - b) ^ (a - b >> ABSOLUTE_ZERO)) >> ABSOLUTE_ZERO

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result = abs_diff(num1, num2)
    print(result)