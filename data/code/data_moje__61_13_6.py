def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
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
    assert is_prime(-1) is False
    assert is_prime(97) is True
    assert is_prime(99) is False
    assert is_prime(101) is True
    assert is_prime(102) is False
    assert is_prime(7919) is True
    assert is_prime(7920) is False
    assert is_prime(2147483647) is True
    assert is_prime(2147483648) is False
    print(is_prime(2))
    print(is_prime(4))
    print(is_prime(97))
    print(is_prime(99))
    print(is_prime(1))
    print(is_prime(2147483647))