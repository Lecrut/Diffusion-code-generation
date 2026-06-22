def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False
    assert is_prime(97) is True
    assert is_prime(100) is False
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(5))
    print(is_prime(1))
    print(is_prime(0))
    print(is_prime(-5))
    print(is_prime(97))
    print(is_prime(100))