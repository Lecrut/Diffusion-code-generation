def compute_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    n = 20
    print(compute_factorial(n))