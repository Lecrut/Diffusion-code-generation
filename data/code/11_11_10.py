def find_duplicate_characters(text):
    from collections import Counter
    char_counts = Counter(text)
    duplicates = {char: count for char, count in char_counts.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_text1 = "hello world"
    sample_text2 = "café résumé naïve"
    sample_text3 = "abcdef"
    sample_text4 = "aabbcc"
    print(find_duplicate_characters(sample_text1))
    print(find_duplicate_characters(sample_text2))
    print(find_duplicate_characters(sample_text3))
    print(find_duplicate_characters(sample_text4))