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
    numbers = [0, 1, 2, 3, 4, 5, 10, 11, 17, 20, 23, 97, 100, 101]
    results = []
    for num in numbers:
        results.append((num, is_prime(num)))
    print(results)