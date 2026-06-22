def digit_generator(number):
    if number == 0:
        yield 0
        return
    is_negative = number < 0
    number = abs(number)
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
    total = sum_digits(sample_number)
    print(digits)
    print(total)