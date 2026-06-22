import re

def extract_digits(text: str) -> tuple:
    digits = re.findall(r'\d+', text)
    return tuple(int(d) for d in digits)

if __name__ == '__main__':
    sample_text = "abc123 def456 ghi789"
    result = extract_digits(sample_text)
    print(result)