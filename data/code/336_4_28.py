def find_duplicates(s):
    char_count = {}
    duplicates = []
    for char in s:
        if char in char_count:
            if char not in duplicates:
                duplicates.append(char)
        else:
            char_count[char] = 0
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string.lower())
    print(result)