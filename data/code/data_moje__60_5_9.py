def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    counter = 1
    while counter <= n:
        result = result * counter
        counter = counter + 1
    return result

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(0))
    print(factorial(3))