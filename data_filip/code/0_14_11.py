def filter_digits(s):
    return [int(char) for char in s if char.isdigit()]

if __name__ == '__main__':
    sample_string = "a1b2c3d4e5"
    print(filter_digits(sample_string))