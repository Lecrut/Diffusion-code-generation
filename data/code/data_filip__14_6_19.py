def has_unique_characters(text):
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    for count in char_freq.values():
        if count > 1:
            return False
    return True

if __name__ == '__main__':
    sample_string = "abcdef"
    result = has_unique_characters(sample_string)
    print(result)