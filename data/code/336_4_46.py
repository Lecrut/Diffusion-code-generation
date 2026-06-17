def find_duplicate_characters(s):
    char_count = {}
    duplicates = []
    for char in s:
        if not (char.isalnum() and len(char) == 1):
            continue
        count = char_count.get(char, 0) + 1
        char_count[char] = count
        if count > 1 and char not in duplicates:
            duplicates.append(char)
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_characters(sample_string)
    print(result)