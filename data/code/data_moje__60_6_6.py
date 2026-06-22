def factorial_iterative(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    assert factorial_iterative(0) == 1
    assert factorial_iterative(1) == 1
    assert factorial_iterative(2) == 2
    assert factorial_iterative(3) == 6
    assert factorial_iterative(5) == 120
    assert factorial_iterative(10) == 3628800
    assert factorial_iterative(1) == 1
    assert factorial_iterative(6) == 720
    assert factorial_iterative(7) == 5040
    assert factorial_iterative(8) == 40320
    assert factorial_iterative(9) == 362880
    assert factorial_iterative(12) == 479001600
    assert factorial_iterative(15) == 1307674368000
    assert factorial_iterative(20) == 2432902008176640000
    print(factorial_iterative(0))
    print(factorial_iterative(1))
    print(factorial_iterative(5))
    print(factorial_iterative(10))
    print(factorial_iterative(20))