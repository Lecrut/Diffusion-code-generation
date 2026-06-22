import re

def extract_digits(text: str) -> list[int]:
    return [int(m) for m in re.findall(r'\d+', text)]

if __name__ == '__main__':
    result = extract_digits("a1b23c456")
    print(result)