import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
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

if __name__ == '__main__':
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(97) == True
    assert is_prime(100) == False
    print(is_prime(17))
    print(is_prime(100))
    print(is_prime(2))
    print(is_prime(1))