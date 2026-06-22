def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5)
    candidate = 3
    while candidate <= sqrt_n:
        if n % candidate == 0:
            return False
        candidate += 2
    return True

if __name__ == '__main__':
    sample_values = [2, 3, 4, 17, 18, 97, 100]
    for value in sample_values:
        result = is_prime(value)
        print(result)