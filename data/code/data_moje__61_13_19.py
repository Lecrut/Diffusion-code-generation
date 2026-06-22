import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (17, True),
        (18, False),
        (97, True),
        (100, False),
        (7919, True),
        (8000, False)
    ]
    for value, expected in test_cases:
        result = is_prime(value)
        assert result == expected, f"Failed for {value}: expected {expected}, got {result}"
        print(f"is_prime({value}) -> {result}")