def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    def check_divisibility(start, step):
        i = start
        while i * i <= n:
            if n % i == 0:
                return False
            i += step
        return True
    
    return check_divisibility(5, 6) and check_divisibility(7, 4)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 10, 11, 13, 17, 19, 23, 29, 31]
    for value in sample_values:
        print(f"{value}: {is_prime(value)}")