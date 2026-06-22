def compress_string(data):
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}" if count > 1 else current_char)
            current_char = char
            count = 1
    
    result.append(f"{current_char}{count}" if count > 1 else current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccddee"
    compressed_output = compress_string(sample_input)
    print(compressed_output)
    
    sample_empty = ""
    print(compress_string(sample_empty))
    
    sample_single = "a"
    print(compress_string(sample_single))
    
    sample_no_repeat = "abcdef"
    print(compress_string(sample_no_repeat))