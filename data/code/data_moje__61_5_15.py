def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        return False
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
    test_values = [1, 2, 3, 4, 17, 18, 97, 100]
    for val in test_values:
        print(f"{val} is prime: {is_prime(val)}")