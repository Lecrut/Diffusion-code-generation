def compute_factorial(n):
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result

if __name__ == '__main__':
    print(compute_factorial(5))
    print(compute_factorial(10))
    print(compute_factorial(0))