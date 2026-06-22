import re

def extract_digits_as_tuple(mixed_string):
    digit_strings = re.findall(r'\d+', mixed_string)
    return tuple(int(digit) for digit in digit_strings)

if __name__ == '__main__':
    sample = "a1b2c3"
    result = extract_digits_as_tuple(sample)
    print(result)