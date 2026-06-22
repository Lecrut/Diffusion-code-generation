from collections import Counter
import string

def find_repeated_chars(text):
    chars_to_filter = set(string.whitespace + string.punctuation)
    cleaned = [char.lower() for char in text if char not in chars_to_filter]
    counts = Counter(cleaned)
    repeated = [char for char, count in counts.items() if count > 1]
    return sorted(repeated)

if __name__ == '__main__':
    sample_text = "Hello, World!   This is a test.  Hheellllooo wwoorrrlllddd!!!"
    result = find_repeated_chars(sample_text)
    print(result)