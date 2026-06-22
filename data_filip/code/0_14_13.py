def filter_digits(s):
    return [int(c) for c in s if c.isdigit()]

if __name__ == '__main__':
    sample_string = "a1b2c3"
    print(filter_digits(sample_string))