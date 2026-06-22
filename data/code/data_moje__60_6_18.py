def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    assert factorial_iterative(0) == 1
    assert factorial_iterative(1) == 1
    assert factorial_iterative(5) == 120
    assert factorial_iterative(10) == 3628800
    assert factorial_iterative(1) == 1
    assert factorial_iterative(2) == 2
    assert factorial_iterative(3) == 6
    assert factorial_iterative(4) == 24
    assert factorial_iterative(6) == 720
    assert factorial_iterative(100) > 0

    print(factorial_iterative(5))
    print(factorial_iterative(10))
    print(factorial_iterative(0))
    print(factorial_iterative(20))