def find_divisors(n):
    if n <= 0:
        return []
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    sample_values = [1, 12, 37, 100, 123456789]
    for value in sample_values:
        result = find_divisors(value)
        print(result)