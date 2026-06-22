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
    sample_values = [28, 100, 13, 1]
    for val in sample_values:
        result = find_divisors(val)
        print(result)