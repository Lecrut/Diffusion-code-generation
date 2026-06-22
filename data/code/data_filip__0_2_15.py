import re

def extract_digits(text: str) -> tuple:
    pattern = r'\d+'
    matches = re.findall(pattern, text)
    return tuple(int(match) for match in matches)

if __name__ == '__main__':
    sample_string = "abc123def456ghi789jkl"
    result = extract_digits(sample_string)
    print(result)