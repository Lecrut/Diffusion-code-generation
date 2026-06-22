def validate_non_negative_integer(value):
    if not isinstance(value, int):
        raise TypeError('Input must be an integer')
    if value < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    return True

def compute_factorial(n):
    validate_non_negative_integer(n)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print(compute_factorial(20))