def find_duplicate_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
    duplicates.sort()
    return duplicates

if __name__ == '__main__':
    sample_text = "programming is fun"
    result = find_duplicate_characters(sample_text)
    print(result)