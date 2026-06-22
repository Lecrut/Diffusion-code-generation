def _compute_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result

def run_validation():
    assert _compute_factorial(0) == 1
    assert _compute_factorial(1) == 1
    assert _compute_factorial(2) == 2
    assert _compute_factorial(3) == 6
    assert _compute_factorial(4) == 24
    assert _compute_factorial(5) == 120
    assert _compute_factorial(6) == 720
    assert _compute_factorial(7) == 5040
    assert _compute_factorial(8) == 40320
    assert _compute_factorial(9) == 362880
    assert _compute_factorial(10) == 3628800
    assert _compute_factorial(12) == 479001600
    assert _compute_factorial(15) == 1307674368000
    assert _compute_factorial(20) == 2432902008176640000

if __name__ == '__main__':
    run_validation()
    print(_compute_factorial(0))
    print(_compute_factorial(1))
    print(_compute_factorial(5))
    print(_compute_factorial(10))
    print(_compute_factorial(25))