def compute_factorial(n):
    result = 1
    i = 1
    while True:
        result *= i
        i += 1
        if i > n:
            break
    return result

if __name__ == '__main__':
    n = 10
    factorial_value = compute_factorial(n)
    print(factorial_value)