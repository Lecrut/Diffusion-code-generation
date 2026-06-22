def digit_generator(number):
    if number < 0:
        raise ValueError('Number must be non-negative')
    if number == 0:
        yield 0
        return
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    for digit in reversed(digits):
        yield digit

def sum_digits(number):
    return sum(digit_generator(number))
if __name__ == '__main__':
    sample_number = 12345
    digits = list(digit_generator(sample_number))
    digit_sum = sum_digits(sample_number)
    print(digits)
    print(digit_sum)