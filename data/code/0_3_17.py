def extract_digits(s):
    result = []
    for char in s:
        if char.isdigit():
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "abc123def45ghi6789"
    print(extract_digits(sample_string))
    empty_string = "no digits here"
    print(extract_digits(empty_string))
    mixed_case = "a1B2c3D4"
    print(extract_digits(mixed_case))