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
    sample_values = [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for value in sample_values:
        print(f"{value}: {is_prime(value)}")