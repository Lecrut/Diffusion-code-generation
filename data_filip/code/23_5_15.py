def compress_string(text):
    if text is None:
        raise TypeError("Input must be a string, not NoneType")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if len(text) == 0:
        return ""
    
    encoded_chars = []
    current_char = text[0]
    current_count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            current_count += 1
        else:
            encoded_chars.append(current_char)
            encoded_chars.append(str(current_count))
            current_char = char
            current_count = 1
    
    encoded_chars.append(current_char)
    encoded_chars.append(str(current_count))
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = compress_string(sample_input)
    print(result)