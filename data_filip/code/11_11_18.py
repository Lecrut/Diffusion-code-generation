import unicodedata
from collections import Counter

def find_duplicate_unicode_chars(text):
    normalized_text = unicodedata.normalize('NFC', text)
    char_counts = Counter(normalized_text)
    duplicates = {char: count for char, count in char_counts.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_text = "café ☕ café café 🌍 🌍"
    result = find_duplicate_unicode_chars(sample_text)
    print(result)