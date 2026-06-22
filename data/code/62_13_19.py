def get_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(list(divisors))

if __name__ == '__main__':
    sample_numbers = [12, 28, 100, 13, 1]
    for num in sample_numbers:
        result = get_divisors(num)
        print(result)