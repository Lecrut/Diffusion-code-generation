import unicodedata

def extract_digits(s):
    return [int(ch) for ch in s if unicodedata.category(ch).startswith('Nd')]

if __name__ == '__main__':
    sample_strings = [
        "abc123def456",
        "hello world",
        "1a2b3c4d5e",
        "no digits here",
        "100 apples and 200 oranges",
        "unicode digits: ²³⁴ (superscripts may not count as Nd)",
        "mixed: 1, 2, 3 and 4"
    ]
    for s in sample_strings:
        print(extract_digits(s))