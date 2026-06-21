def find_first_non_repeating(s):
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    for char in s:
        if char_freq[char] == 1:
            return char
    
    return None

if __name__ == '__main__':
    sample_string = "programming"
    result = find_first_non_repeating(sample_string)
    print(f"The first non-repeating character is: {result}")