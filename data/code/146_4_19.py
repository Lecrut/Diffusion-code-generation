def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for idx, char in enumerate(s):
        if char_count[char] == 1:
            return idx
    return -1

if __name__ == '__main__':
    sample_string = "programming"
    result = first_non_repeating_char(sample_string)
    print(f"The index of the first non-repeating character is: {result}")