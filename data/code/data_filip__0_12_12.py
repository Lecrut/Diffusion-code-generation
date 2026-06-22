def extract_digits(input_string):
    result = []
    for char in input_string:
        if '0' <= char <= '9':
            result.append(char)
    return result

if __name__ == '__main__':
    sample_data = "User123@Example#45.67-xyz"
    extracted = extract_digits(sample_data)
    print(extracted)