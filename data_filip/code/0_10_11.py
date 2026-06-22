import re

def extract_digits(input_string: str) -> list[int]:
    matches = re.findall('\\d+', input_string)
    return [int(match) for match in matches]
if __name__ == '__main__':
    sample_text = 'abc123def456ghi789'
    result = extract_digits(sample_text)
    print(result)