def get_divisors(number):
    if number <= 0:
        return []
    divisors = set()
    i = 1
    while i * i <= number:
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
        i += 1
    return sorted(list(divisors))

if __name__ == '__main__':
    sample_number = 100
    result = get_divisors(sample_number)
    print(result)