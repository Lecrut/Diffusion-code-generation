def count_characters(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    char_count = {}
    for char in s:
        if len(char) != 1:
            continue
        
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

if __name__ == '__main__':
    sample_string = "hello world"
    print(count_characters(sample_string))