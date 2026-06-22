def get_divisors(number):
    if number < 1:
        raise ValueError("Number must be a positive integer.")
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_number = 28
    divisors = get_divisors(sample_number)
    print(divisors)