def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(97) == True
    assert is_prime(100) == False
    print(is_prime(97))
    print(is_prime(100))