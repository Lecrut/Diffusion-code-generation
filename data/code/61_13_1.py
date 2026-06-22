import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(18) is False
    assert is_prime(97) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(25) is False
    assert is_prime(29) is True
    print(is_prime(17))
    print(is_prime(18))
    print(is_prime(97))
    print(is_prime(1))
    print(is_prime(-5))