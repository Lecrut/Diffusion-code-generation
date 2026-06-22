from collections import Counter

def find_repeated_chars(s):
    counts = Counter(s)
    repeated = [char for char, count in counts.items() if count > 1]
    return sorted(repeated)

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "programming",
        "abcdef",
        "aabbccddeeff",
        "xyz"
    ]
    for s in sample_strings:
        result = find_repeated_chars(s)
        print(result)