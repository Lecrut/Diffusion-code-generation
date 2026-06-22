def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

if __name__ == '__main__':
    result = get_divisors(60)
    print(result)