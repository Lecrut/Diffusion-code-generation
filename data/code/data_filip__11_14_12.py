import collections
import re

def find_duplicate_characters(text: str) -> dict[str, int]:
    char_counts = collections.Counter(text)
    duplicates = {char: count for char, count in char_counts.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_text = "programming is awesome"
    result = find_duplicate_characters(sample_text)
    print(result)