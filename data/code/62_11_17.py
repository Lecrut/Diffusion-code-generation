def get_divisors(n):
    if n == 0:
        return [0]
    n = abs(n)
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return sorted(divisors)

if __name__ == '__main__':
    result1 = get_divisors(28)
    print(result1)
    result2 = get_divisors(13)
    print(result2)
    result3 = get_divisors(100)
    print(result3)