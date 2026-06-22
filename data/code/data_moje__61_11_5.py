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
    sample_values = [0, 1, 2, 3, 4, 5, 16, 17, 18, 19, 97, 98, 99, 100, 7919, 8000, 104729]
    for value in sample_values:
        print(f"{value}: {is_prime(value)}")