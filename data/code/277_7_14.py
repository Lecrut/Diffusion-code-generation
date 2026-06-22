def count_digits(number):
    if number == 0:
        return 1
    digits = 0
    if number < 0:
        number = -number
    while number > 0:
        number //= 10
        digits += 1
    return digits

if __name__ == '__main__':
    sample_number = -12345
    digit_count = count_digits(sample_number)
    print(digit_count)