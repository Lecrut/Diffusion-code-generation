def get_divisors(n: int) -> list[int]:
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors

if __name__ == '__main__':
    result = get_divisors(999999)
    print(result)