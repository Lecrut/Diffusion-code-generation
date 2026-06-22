import re

def extract_digits(text):
    return [int(match) for match in re.findall(r'\d+', text)]

if __name__ == '__main__':
    result = extract_digits("abc123def456ghi789jkl012")
    print(result)