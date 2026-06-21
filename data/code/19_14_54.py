def is_prime(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        raise ValueError("Number is not prime")
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 23, 24, 29]
    for value in sample_values:
        try:
            print(f"{value}: {is_prime(value)}")
        except ValueError as e:
            print(f"{value}: {e}")