def compress_string(input_str):
    if not input_str:
        return ""
    
    result = []
    current_char = input_str[0]
    count = 1
    
    for i in range(1, len(input_str)):
        char = input_str[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
    
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabbcc"
    compressed = compress_string(sample_input)
    print(compressed)