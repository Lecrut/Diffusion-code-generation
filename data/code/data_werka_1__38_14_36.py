def find_repeated_characters(s):
    char_map = {}
    for char in s:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    repeated_chars = [char for char, count in char_map.items() if count > 1]
    return sorted(repeated_chars)

if __name__ == '__main__':
    sample_string = "characters"
    result = find_repeated_characters(sample_string)
    print(result)