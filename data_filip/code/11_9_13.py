import string
import collections

def find_repeated_chars(s):
    cleaned = "".join(ch.lower() for ch in s if ch not in string.whitespace and ch not in string.punctuation)
    counts = collections.Counter(cleaned)
    return sorted([ch for ch, count in counts.items() if count > 1])

if __name__ == '__main__':
    sample = "Hello, World! Hello Python."
    result = find_repeated_chars(sample)
    print(result)