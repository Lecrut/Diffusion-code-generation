def compute_factorial(n):
    if n < 0:
        return 0
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

if __name__ == '__main__':
    print(compute_factorial(5))
    print(compute_factorial(0))
    print(compute_factorial(1))