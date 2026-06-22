def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    test_numbers = [0, 1, 2, 3, 4, 17, 18, 19, 97, 100, 101, 113, 1000000007]
    for num in test_numbers:
        print(f"{num}: {is_prime(num)}")