def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    def check_divisibility(limit, step):
        for i in range(3, limit, step):
            if n % i == 0:
                return False
        return True

    return check_divisibility(int(n**0.5) + 1, 2)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for value in sample_values:
        print(f"{value}: {is_prime(value)}")