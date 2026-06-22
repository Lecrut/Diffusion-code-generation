import re

def extract_digits_as_integers(s):
    return [int(x) for x in re.findall(r'\d+', s)]

if __name__ == '__main__':
    sample = "abc123def45ghi678"
    print(extract_digits_as_integers(sample))