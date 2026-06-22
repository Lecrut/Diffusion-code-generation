import re

def extract_digits(mixed_string):
    digits = re.findall(r'\d+', mixed_string)
    return tuple(int(d) for d in digits)

if __name__ == '__main__':
    sample_string = "abc123def456ghi789"
    result = extract_digits(sample_string)
    print(result)