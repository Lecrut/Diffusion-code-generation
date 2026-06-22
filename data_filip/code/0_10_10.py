import re

def extract_digits(text: str) -> list[int]:
    matches = re.findall('\\d+', text)
    return [int(match) for match in matches]
if __name__ == '__main__':
    sample_text = 'abc123def456ghi789jkl'
    result = extract_digits(sample_text)
    print(result)