def find_divisors(number):
    if number <= 0:
        raise ValueError('Number must be positive')
    divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)
if __name__ == '__main__':
    test_numbers = [12, 25, 36, 49, 100]
    for num in test_numbers:
        divisors = find_divisors(num)
        print(f'Divisors of {num}: {divisors}')