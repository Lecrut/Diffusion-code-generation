from collections import Counter

def find_duplicate_chars(text: str) -> list:
    lower_text = text.lower()
    char_counts = Counter(lower_text)
    duplicates = sorted({char for char, count in char_counts.items() if count > 1})
    return duplicates

if __name__ == '__main__':
    sample_text = "Programming"
    result = find_duplicate_chars(sample_text)
    print(result)