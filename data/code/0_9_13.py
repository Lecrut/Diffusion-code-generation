def extract_digits(mixed_string):
    digit_gen = (char for char in mixed_string if char.isdigit())
    return ''.join(digit_gen)

if __name__ == '__main__':
    sample = "a1b2c3d4e5"
    result = extract_digits(sample)
    print(result)