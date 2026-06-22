def get_divisors(n):
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return sorted(list(divisors))

if __name__ == '__main__':
    number = 36
    result = get_divisors(number)
    print(result)