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
    test_cases = {2: True, 3: True, 4: False, 5: True, 17: True, 18: False, 19: True, 20: False, 23: True, 29: True, 31: True}
    for num, expected in test_cases.items():
        result = is_prime(num)
        print(f"{num} is prime: {result}, Expected: {expected}")