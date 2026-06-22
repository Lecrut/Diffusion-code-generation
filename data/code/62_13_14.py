def get_divisors(n: int) -> list[int]:
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
    sample_number = 100
    result = get_divisors(sample_number)
    print(result)