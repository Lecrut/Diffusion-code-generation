def find_divisors(n):
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return sorted(divisors)

if __name__ == '__main__':
    print(find_divisors(1024))