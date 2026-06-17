def find_duplicate_characters(s):
    char_count = {}
    duplicates = []
    for char in s:
        if char in char_count:
            if char not in duplicates:
                duplicates.append(char)
        else:
            char_count[char] = 1
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_characters(sample_string)
    print(result)