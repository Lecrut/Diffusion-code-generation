def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print(factorial_iterative(0))
    print(factorial_iterative(1))
    print(factorial_iterative(5))
    print(factorial_iterative(10))
    print(factorial_iterative(20))