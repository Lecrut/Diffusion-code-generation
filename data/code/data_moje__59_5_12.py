def digit_generator(number):
    if number < 0:
        number = -number
    if number == 0:
        yield 0
        return
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    for d in reversed(digits):
        yield d

def sum_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_number = 12345
    digits_list = list(digit_generator(sample_number))
    total = sum_digits(sample_number)
    print(digits_list)
    print(total)