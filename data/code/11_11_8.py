from collections import Counter
from typing import Dict

def find_duplicate_chars(text: str) -> Dict[str, int]:
    char_counts = Counter(text)
    duplicates = {char: count for char, count in char_counts.items() if count > 1}
    return duplicates
if __name__ == '__main__':
    sample_text = 'Hello, World! 世界 Hello'
    result = find_duplicate_chars(sample_text)
    print(result)