def find_duplicates(s):
    char_count = {}
    duplicates = []
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1 and not any(char == d for d in duplicates):
            duplicates.append(char)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)