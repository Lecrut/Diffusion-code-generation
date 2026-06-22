def get_divisors(n):
    if n == 0:
        return []
    if n < 0:
        n = -n
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    print(get_divisors(0))
    print(get_divisors(28))
    print(get_divisors(-12))