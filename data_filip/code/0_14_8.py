def extract_digits_as_ints(s):
    return [int(c) for c in s if c.isdigit()]

if __name__ == '__main__':
    sample_string = "a1b2c3!@#"
    result = extract_digits_as_ints(sample_string)
    print(result)