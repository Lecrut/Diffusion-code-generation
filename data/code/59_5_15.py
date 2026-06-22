def digit_generator(number):
    if number < 0:
        number = -number
    if number == 0:
        yield 0
        return
    while number > 0:
        yield number % 10
        number //= 10

def sum_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_number = 12345
    print(sum_digits(sample_number))
    digits = list(digit_generator(sample_number))
    print(digits)