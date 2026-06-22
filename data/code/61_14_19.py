def is_prime(n):
    if n < 2:
        return False
    if n < 4:
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
    sample_numbers = [1, 2, 3, 4, 10, 11, 13, 17, 20, 29, 50, 97, 100, 101, 103]
    for num in sample_numbers:
        print(f"{num}: {is_prime(num)}")