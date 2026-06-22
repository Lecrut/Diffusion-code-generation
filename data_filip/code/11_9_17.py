import string

def find_repeated_chars(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    counts = {}
    for char in cleaned:
        counts[char] = counts.get(char, 0) + 1
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample = "Hello, World! Hello."
    result = find_repeated_chars(sample)
    print(result)