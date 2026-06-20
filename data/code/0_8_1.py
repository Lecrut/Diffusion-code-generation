def extract_digit_sum(mixed_string):
    total = 0
    for char in mixed_string:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_input = "abc123xyz456"
    result = extract_digit_sum(sample_input)
    print(result)