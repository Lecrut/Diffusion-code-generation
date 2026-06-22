def get_divisors(n: int) -> list:
    if n == 0:
        return []
    if n < 0:
        n = -n
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors

if __name__ == '__main__':
    test_value = 0
    result = get_divisors(test_value)
    print(result)
    test_value = 12
    result = get_divisors(test_value)
    print(result)
    test_value = -15
    result = get_divisors(test_value)
    print(result)