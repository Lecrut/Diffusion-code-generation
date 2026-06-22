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
    sample_values = [12, 100, 1, 0, -5, 97]
    for value in sample_values:
        result = find_divisors(value)
        print(f"Divisors of {value}: {result}")