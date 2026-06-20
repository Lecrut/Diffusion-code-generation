def validate_input(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Both inputs must be integers.')

def multiply(a, b):
    validate_input(a, b)
    result = 0
    negative_result = a < 0 != b < 0
    a, b = (abs(a), abs(b))
    while b:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    return -result if negative_result else result
if __name__ == '__main__':
    print(multiply(5, 3))
    print(multiply(-5, 3))
    print(multiply(-4, -2))
    print(multiply(0, 5))
    print(multiply(-10, 0))