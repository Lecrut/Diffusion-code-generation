def extract_digits_from_mixed_string(input_string):
    digit_list = []
    for char in input_string:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            digit_list.append(char)
    return "".join(digit_list)

if __name__ == '__main__':
    sample_mixed_string = "abc123xyz45!67"
    result = extract_digits_from_mixed_string(sample_mixed_string)
    print(result)