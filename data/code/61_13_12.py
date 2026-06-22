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
    test_cases = [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (97, True),
        (1, False),
        (0, False),
        (-5, False),
        (999999937, True)
    ]
    for value, expected in test_cases:
        result = is_prime(value)
        assert result == expected, f"Failed for {value}: expected {expected}, got {result}"
        print(f"is_prime({value}) = {result}")