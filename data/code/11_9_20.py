import string

def find_repeated_characters(s):
    cleaned = ''.join(ch for ch in s if ch not in string.whitespace and ch not in string.punctuation)
    lower_cleaned = cleaned.lower()
    seen = set()
    repeated = set()
    for ch in lower_cleaned:
        if ch in seen:
            repeated.add(ch)
        else:
            seen.add(ch)
    return sorted(repeated)

if __name__ == '__main__':
    sample = "Hello, World! Hello Python."
    result = find_repeated_characters(sample)
    print(result)