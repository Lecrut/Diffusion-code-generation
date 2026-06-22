def get_divisors(n):
    return [i for i in range(1, int(n ** 0.5) + 1) if n % i == 0] + [n // i for i in range(1, int(n ** 0.5) + 1) if n % i == 0 and i * i != n] if n > 0 else []

if __name__ == '__main__':
    target = 60
    result = get_divisors(target)
    result.sort()
    print(result)