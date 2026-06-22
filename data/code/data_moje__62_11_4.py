def find_divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_values = [1, 12, 28, 100, 360, 997]
    for value in sample_values:
        result = find_divisors(value)
        print(f"Divisors of {value}: {result}")