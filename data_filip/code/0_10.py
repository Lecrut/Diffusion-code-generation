import re

def extract_digits(mixed_string):
    matches = re.findall(r'\d+', mixed_string)
    return [int(m) for m in matches]

if __name__ == '__main__':
    sample_input = "abc123def456ghi789jkl0"
    result = extract_digits(sample_input)
    print(result)