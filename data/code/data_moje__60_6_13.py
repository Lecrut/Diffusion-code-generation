def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(5))
    print(factorial(10))
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(6) == 720
    assert factorial(12) == 479001600
    assert factorial(15) == 1307674368000
    assert factorial(20) == 2432902008176640000
    print("All assertions passed")