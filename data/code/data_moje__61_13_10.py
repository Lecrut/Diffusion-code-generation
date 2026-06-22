def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(9) is False
    assert is_prime(11) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False
    print(is_prime(29))
    print(is_prime(25))
    print(is_prime(97))