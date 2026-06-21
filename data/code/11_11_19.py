from collections import Counter

def find_duplicate_characters(text):
    char_counts = Counter(text)
    duplicates = {char: count for char, count in char_counts.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_text_1 = "hello world"
    sample_text_2 = "abcdef"
    sample_text_3 = "äöüÄÖÜß"
    sample_text_4 = "aabbc"
    sample_text_5 = "你好世界你好"
    sample_text_6 = "café"
    print(find_duplicate_characters(sample_text_1))
    print(find_duplicate_characters(sample_text_2))
    print(find_duplicate_characters(sample_text_3))
    print(find_duplicate_characters(sample_text_4))
    print(find_duplicate_characters(sample_text_5))
    print(find_duplicate_characters(sample_text_6))