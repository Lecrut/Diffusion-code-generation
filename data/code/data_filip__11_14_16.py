def find_duplicate_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    duplicates = {char: count for char, count in char_count.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_text = "hello world this is a test string with some duplicate characters"
    result = find_duplicate_characters(sample_text)
    print(result)