def find_repeated_characters(input_string):
    char_count = {}
    repeated_chars = []
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in input_string:
        if char_count[char] > 1:
            if char not in repeated_chars:
                repeated_chars.append(char)
    return repeated_chars

if __name__ == '__main__':
    result = find_repeated_characters("programming")
    print(result)