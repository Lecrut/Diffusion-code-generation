def get_divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

if __name__ == '__main__':
    print(get_divisors(60))