def find_divisors(number):
    if number <= 0:
        return []
    divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)
if __name__ == '__main__':
    test_number = 28
    divisors = find_divisors(test_number)
    print(f'Divisors of {test_number}: {divisors}')