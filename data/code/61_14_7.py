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
    sample_numbers = [1, 2, 3, 4, 5, 10, 13, 17, 18, 23, 25, 29, 97, 100]
    for number in sample_numbers:
        result = is_prime(number)
        print(f"{number}: {result}")