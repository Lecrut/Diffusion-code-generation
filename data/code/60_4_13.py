def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 10]
    for value in test_values:
        print(value, factorial(value))