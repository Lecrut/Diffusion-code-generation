def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    samples = [1, 2, 3, 4, 17, 25, 97, 100]
    results = {num: is_prime(num) for num in samples}
    for num, result in results.items():
        print(f"{num}: {result}")