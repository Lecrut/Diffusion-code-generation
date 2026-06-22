def compute_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
if __name__ == '__main__':
    n = 20
    factorial_result = compute_factorial(n)
    print(factorial_result)