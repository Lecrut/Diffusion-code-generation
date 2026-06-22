def get_divisors(n):
    if n <= 0:
        return []
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_value = 100
    result = get_divisors(sample_value)
    print(result)