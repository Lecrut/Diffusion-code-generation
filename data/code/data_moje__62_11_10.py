def get_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)

if __name__ == '__main__':
    print(get_divisors(12))
    print(get_divisors(28))
    print(get_divisors(100))