def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    check_map = {5: 6, 7: 4}
    for start, step in check_map.items():
        i = start
        while i * i <= n:
            if n % i == 0:
                return False
            i += step
    return True
if __name__ == '__main__':
    sample_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for value in sample_values:
        print(f'{value}: {is_prime(value)}')