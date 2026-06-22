def count_digits(number):
    if number == 0:
        return 1
    count = 0
    abs_number = abs(number)
    while abs_number != 0:
        abs_number //= 10
        count += 1
    return count

if __name__ == '__main__':
    sample_values = [0, 5, 12345, -98765]
    for value in sample_values:
        print(f"Number of digits in {value}: {count_digits(value)}")