def get_divisors(n):
    if n == 0:
        return []
    divisors = []
    start = 1
    if n < 0:
        n = -n
        start = -1
    for i in range(start, n + 1):
        if i != 0 and n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    print(get_divisors(0))
    print(get_divisors(6))
    print(get_divisors(-6))
    print(get_divisors(1))
    print(get_divisors(13))