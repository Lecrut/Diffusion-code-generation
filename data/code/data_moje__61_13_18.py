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
    test_values = [2, 3, 4, 5, 16, 17, 18, 19, 23, 24, 25, 29, 97, 100]
    for value in test_values:
        print(f"{value}: {is_prime(value)}")
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(16)
    assert is_prime(17)
    assert not is_prime(18)
    assert is_prime(19)
    assert is_prime(23)
    assert not is_prime(24)
    assert not is_prime(25)
    assert is_prime(29)
    assert is_prime(97)
    assert not is_prime(100)
    assert not is_prime(1)
    assert not is_prime(0)
    assert not is_prime(-5)