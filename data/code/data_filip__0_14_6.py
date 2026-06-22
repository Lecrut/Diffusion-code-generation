def extract_digits(s):
    return [int(c) for c in s if c.isdigit()]

if __name__ == '__main__':
    sample_string = "a1b2c3"
    result = extract_digits(sample_string)
    print(result)