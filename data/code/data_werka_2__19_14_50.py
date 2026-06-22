def is_prime(n):
    if n <= 1:
        raise ValueError("Input must be greater than 1")
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
    sample_values = [10, 13, 17, 19, 20, 23, 24, 29, 31, 37, 41]
    for value in sample_values:
        try:
            print(f"{value}: {is_prime(value)}")
        except ValueError as e:
            print(f"Error: {e}")