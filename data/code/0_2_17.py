import re

def extract_digits_as_tuple(mixed_string):
    digits = re.findall(r'\d+', mixed_string)
    return tuple(int(d) for d in digits)

if __name__ == '__main__':
    sample = "abc123def45gh678ij9"
    result = extract_digits_as_tuple(sample)
    print(result)