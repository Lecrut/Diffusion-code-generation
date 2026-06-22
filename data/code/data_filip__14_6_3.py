def find_first_unique_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

if __name__ == '__main__':
    sample_string = "swiss"
    result = find_first_unique_character(sample_string)
    print(result)