def get_divisors(number):
    if number <= 0:
        return []
    divisors = set()
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    return sorted(divisors)
if __name__ == '__main__':
    sample_numbers = [12, 28, 13, 100, 1]
    for num in sample_numbers:
        result = get_divisors(num)
        print(f'Divisors of {num}: {result}')