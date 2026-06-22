import re

def extract_digits(s):
    return [int(x) for x in re.findall(r'\d+', s)]

if __name__ == '__main__':
    sample_text = "abc123def4567gh89jkl001"
    result = extract_digits(sample_text)
    print(result)