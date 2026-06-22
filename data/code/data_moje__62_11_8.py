def get_divisors(n):
    if n <= 0:
        return []
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
    sample_value = 28
    result = get_divisors(sample_value)
    print(result)