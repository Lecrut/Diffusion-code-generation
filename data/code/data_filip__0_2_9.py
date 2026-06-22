import re

def extract_digits(s: str) -> tuple[int, ...]:
    return tuple(int(digit) for digit in re.findall(r'\d+', s))

if __name__ == '__main__':
    sample_text = "abc123 def456!@#789"
    result = extract_digits(sample_text)
    print(result)