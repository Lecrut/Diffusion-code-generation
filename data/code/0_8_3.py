def sum_of_digits(mixed_string):
    total = 0
    for char in mixed_string:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_input = "abc123xyz45"
    result = sum_of_digits(sample_input)
    print(result)