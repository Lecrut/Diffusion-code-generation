def extract_digits(s):
    result = []
    for char in s:
        if '0' <= char <= '9':
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "Hello123World456!789"
    extracted = extract_digits(sample_string)
    print(extracted)