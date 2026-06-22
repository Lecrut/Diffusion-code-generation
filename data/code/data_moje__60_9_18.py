NEGATIVE_THRESHOLD = -1
START_MULTIPLIER = 2
INITIAL_PRODUCT = 1

def factorial(n):
    if n <= NEGATIVE_THRESHOLD:
        raise ValueError("Factorial is not defined for negative numbers")
    result = INITIAL_PRODUCT
    index = START_MULTIPLIER
    while index <= n:
        result *= index
        index += 1
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 10, 15]
    for val in test_values:
        print(factorial(val))