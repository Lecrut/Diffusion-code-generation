def detect_duplicate_chars(text):
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    duplicates = {char: count for char, count in char_counts.items() if count > 1}
    return duplicates
if __name__ == '__main__':
    sample_text = 'hello world programming python python'
    result = detect_duplicate_chars(sample_text)
    print(result)