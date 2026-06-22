def count_characters(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

if __name__ == '__main__':
    sample_string = "hello world"
    result = count_characters(sample_string)
    print(result)