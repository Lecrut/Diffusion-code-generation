import re

def extract_digits(s):
    matches = re.findall(r'\d+', s)
    return [int(x) for x in matches]

if __name__ == '__main__':
    sample_input = "abc123def45gh67890xyz"
    result = extract_digits(sample_input)
    print(result)