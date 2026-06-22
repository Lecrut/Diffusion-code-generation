from collections import Counter

def find_duplicate_characters(text):
    if not isinstance(text, str):
        return {}
    char_counts = Counter(text)
    duplicates = {char: count for char, count in char_counts.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_text = "Hello, World! 你好世界"
    result = find_duplicate_characters(sample_text)
    print(result)