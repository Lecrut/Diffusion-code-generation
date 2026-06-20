from collections import Counter

def find_repeated_characters(s: str) -> list:
    counts = Counter(s)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "programming",
        "abcdef",
        "aabbc",
        ""
    ]
    for s in sample_strings:
        result = find_repeated_characters(s)
        print(result)