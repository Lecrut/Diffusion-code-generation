def get_divisors(number):
    if number == 0:
        return []
    divisors = []
    limit = abs(number)
    for i in range(1, limit + 1):
        if limit % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    sample_number = 36
    result = get_divisors(sample_number)
    print(result)