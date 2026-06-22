def get_divisors(number):
    if number <= 0:
        raise ValueError('Number must be a positive integer.')
    divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)
if __name__ == '__main__':
    test_numbers = [12, 28, 100, 13]
    for num in test_numbers:
        result = get_divisors(num)
        print(result)