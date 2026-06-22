def compress_string(input_str):
    if not input_str:
        return ""
    
    result = []
    count = 1
    current_char = input_str[0]
    
    for i in range(1, len(input_str)):
        char = input_str[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
            
    result.append(current_char + str(count))
    
    compressed = "".join(result)
    
    if len(compressed) < len(input_str):
        return compressed
    else:
        return input_str

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    print(compress_string(sample_input))