def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char, count in char_count.items():
        if count == 1:
            return char
    
    return None

if __name__ == '__main__':
    sample_string = "programming"
    result = first_non_repeating_char(sample_string)
    print(f"The first non-repeating character in '{sample_string}' is: {result}")