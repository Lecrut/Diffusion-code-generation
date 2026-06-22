def get_sorted_divisors(n: int) -> list[int]:
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
    print(get_sorted_divisors(28))
    print(get_sorted_divisors(36))
    print(get_sorted_divisors(13))