def find_duplicate_chars(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    duplicates = [char for char, count in char_count.items() if count > 1]
    return sorted(duplicates)

if __name__ == '__main__':
    sample_text = "hello world"
    result = find_duplicate_chars(sample_text)
    print(result)