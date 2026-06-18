def find_duplicate_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1 and not any(char == d for d in duplicates):
            duplicates.append(char)
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_chars(sample_string)
    print(result)