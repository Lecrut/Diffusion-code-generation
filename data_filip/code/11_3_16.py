from collections import Counter

def count_repeated_chars(text: str) -> dict:
    counts = Counter(text)
    return {char: freq for char, freq in counts.items() if freq > 1}

if __name__ == '__main__':
    sample_text = "aabbccddeeffggg"
    result = count_repeated_chars(sample_text)
    print(result)