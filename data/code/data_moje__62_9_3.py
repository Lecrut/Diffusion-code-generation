def get_divisors(n):
    if n == 0:
        return []
    if n < 0:
        n = -n
    divisors = []
    large_divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                large_divisors.append(n // i)
        i += 1
    divisors.extend(reversed(large_divisors))
    return divisors

if __name__ == '__main__':
    number = 36
    result = get_divisors(number)
    print(result)