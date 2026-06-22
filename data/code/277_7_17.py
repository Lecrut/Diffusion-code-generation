def count_digits(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count

if __name__ == '__main__':
    sample_number = -12345
    digit_count = count_digits(sample_number)
    print(digit_count)