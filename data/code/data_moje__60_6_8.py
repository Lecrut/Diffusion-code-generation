import sys

def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    test_cases = [0, 1, 2, 5, 10, 20, 50]
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000
    assert factorial(50) == 30414093201713378043612608166064768844377641568960512000000000000
    for n in test_cases:
        print(factorial(n))