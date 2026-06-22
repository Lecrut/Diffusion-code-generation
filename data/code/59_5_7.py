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
    for digit in reversed(digits):
        yield digit

def sum_digits_generator(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_value = 12345
    digits_list = list(digit_generator(sample_value))
    digits_sum = sum_digits_generator(sample_value)
    print(digits_list)
    print(digits_sum)