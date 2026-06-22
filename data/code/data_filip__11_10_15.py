def find_repeated_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    repeated = [char for char, count in char_count.items() if count > 1]
    return repeated

if __name__ == '__main__':
    sample_string = "aabbccddeeffg"
    result = find_repeated_characters(sample_string)
    print(result)