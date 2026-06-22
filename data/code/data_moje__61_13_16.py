import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    test_cases = [0, 1, 2, 3, 4, 5, 17, 18, 97, 98, 99, 100, 7919, 7920]
    for n in test_cases:
        result = is_prime(n)
        print(f"{n} is prime: {result}")
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(17) is True
    assert is_prime(97) is True
    assert is_prime(7919) is True
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(18) is False
    assert is_prime(100) is False
    assert is_prime(7920) is False