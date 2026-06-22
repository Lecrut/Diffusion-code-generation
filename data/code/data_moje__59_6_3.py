def digit_sum(number_string):
    total = 0
    for char in number_string:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_number = "12345"
    result = digit_sum(sample_number)
    print(result)
    another_sample = "9876543210"
    print(digit_sum(another_sample))
    print(digit_sum("000111"))