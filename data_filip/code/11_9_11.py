import string

def find_repeated_chars(text: str) -> list:
    cleaned = text.translate(str.maketrans('', '', string.whitespace + string.punctuation))
    lower_text = cleaned.lower()
    seen = {}
    for char in lower_text:
        seen[char] = seen.get(char, 0) + 1
    repeated = [char for char, count in seen.items() if count > 1]
    return sorted(repeated)

if __name__ == '__main__':
    sample = "Hello, World! This is a test string."
    result = find_repeated_chars(sample)
    print(result)