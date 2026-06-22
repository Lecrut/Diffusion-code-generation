from collections import Counter

def find_repeated_chars(text: str) -> dict:
    char_counts = Counter(text)
    return {char: count for char, count in char_counts.items() if count > 1}

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_chars(sample_string)
    print(result)