import math

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(18) is False
    assert is_prime(97) is True
    assert is_prime(100) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False
    print(is_prime(7))
    print(is_prime(8))
    print(is_prime(11))
    print(is_prime(15))
    print(is_prime(29))
    print(is_prime(30))