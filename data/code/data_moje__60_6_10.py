def factorial(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(5))
    print(factorial(10))
    print(factorial(20))
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000
    assert factorial(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000