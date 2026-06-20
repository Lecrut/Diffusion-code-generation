import re

def extract_digits(s):
    return [int(x) for x in re.findall(r'\d+', s)]

if __name__ == '__main__':
    sample = "abc123def45ghi6789jkl0mno"
    result = extract_digits(sample)
    print(result)