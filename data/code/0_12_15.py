def extract_digits(s):
    result = []
    for char in s:
        if '0' <= char <= '9':
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "a1b2!c3 d4@5"
    digits = extract_digits(sample_string)
    print(digits)