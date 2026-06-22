import re

def extract_digits_as_tuple(text):
    digits = re.findall(r'\d+', text)
    return tuple(int(d) for d in digits)

if __name__ == '__main__':
    sample = "abc123def456ghi789jkl0"
    result = extract_digits_as_tuple(sample)
    print(result)