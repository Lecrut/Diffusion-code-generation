def factorial(n):
    if n < 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    test_cases = [0, 1, 5, 10]
    for num in test_cases:
        print(factorial(num))