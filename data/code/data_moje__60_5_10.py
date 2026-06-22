def compute_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == '__main__':
    values = [0, 1, 5, 10]
    for val in values:
        print(compute_factorial(val))