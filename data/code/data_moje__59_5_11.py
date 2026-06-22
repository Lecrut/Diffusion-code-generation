def digit_generator(number):
    if number < 0:
        number = -number
    while number > 0:
        yield number % 10
        number //= 10

def sum_of_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_number = 12345
    digits_list = list(digit_generator(sample_number))
    total_sum = sum_of_digits(sample_number)
    print(digits_list)
    print(total_sum)