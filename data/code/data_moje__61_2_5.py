def is_prime(n):
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
    sample_values = [0, 1, 2, 10, 11, 15, 17, 97, 100]
    results = [(num, is_prime(num)) for num in sample_values]
    for num, prime in results:
        print(f"is_prime({num}) = {prime}")