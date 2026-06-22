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
    sample_numbers = [2, 17, 100, 7919, 104729]
    results = []
    for number in sample_numbers:
        results.append(is_prime(number))
    for number, result in zip(sample_numbers, results):
        print(f"{number}: {result}")