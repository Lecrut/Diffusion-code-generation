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
    samples = [1, 2, 3, 4, 5, 10, 17, 18, 19, 20, 25, 29, 30, 97, 98, 100, 101, 1000, 1009, 1013]
    results = {num: is_prime(num) for num in samples}
    print(results)