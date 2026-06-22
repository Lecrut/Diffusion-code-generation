def find_divisors(n):
    if n <= 0:
        return []
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    print(find_divisors(28))
    print(find_divisors(100))
    print(find_divisors(7))
    print(find_divisors(1))