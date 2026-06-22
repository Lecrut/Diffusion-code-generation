import re

def extract_digits(s: str) -> list[int]:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    matches = re.findall(r'\d+', s)
    return [int(m) for m in matches]

if __name__ == '__main__':
    result = extract_digits("abc123def456ghi789")
    print(result)