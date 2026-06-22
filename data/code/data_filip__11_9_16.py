import string

def find_repeated_characters(s):
    cleaned = ''.join(c for c in s if c not in string.whitespace and c not in string.punctuation)
    lower_cleaned = cleaned.lower()
    seen = set()
    repeated = set()
    for char in lower_cleaned:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return sorted(repeated)

if __name__ == '__main__':
    sample = "Hello, World! Hello Python. python is great."
    result = find_repeated_characters(sample)
    print(result)