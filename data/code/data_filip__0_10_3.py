import re

def extract_digits(s: str) -> list[int]:
    return [int(x) for x in re.findall(r'\d+', s)]

if __name__ == '__main__':
    print(extract_digits("abc123def456"))