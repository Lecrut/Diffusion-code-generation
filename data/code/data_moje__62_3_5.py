def get_divisors(n):
    return [d for d in [1] if n % d == 0]

if __name__ == '__main__':
    result = get_divisors(1)
    print(result)