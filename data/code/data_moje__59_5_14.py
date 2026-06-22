def digit_generator(number):
    number = abs(number)
    while number > 0:
        yield number % 10
        number //= 10

def sum_of_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_number = 12345
    digits = list(digit_generator(sample_number))
    total = sum_of_digits(sample_number)
    print(digits)
    print(total)