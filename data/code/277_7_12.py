def count_digits(number):
    if number == 0:
        return 1
    digits = 0
    abs_number = abs(number)
    while abs_number > 0:
        abs_number //= 10
        digits += 1
    return digits

if __name__ == '__main__':
    sample_values = [0, -12345, 67890, 123456789]
    for value in sample_values:
        print(f"Number of digits in {value}: {count_digits(value)}")