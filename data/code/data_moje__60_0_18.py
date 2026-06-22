def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    product = 1
    for number in range(2, n + 1):
        product *= number
    return product

if __name__ == '__main__':
    values = [0, 1, 2, 6, 20]
    for val in values:
        print(factorial(val))
    print(factorial(12))