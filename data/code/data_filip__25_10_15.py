def compress_string(input_str):
    if not input_str:
        return ""
    
    compressed = []
    current_char = input_str[0]
    count = 1
    length = len(input_str)
    
    for i in range(1, length):
        char = input_str[i]
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    compressed.append(f"{current_char}{count}")
    
    result = "".join(compressed)
    if len(result) >= length:
        return input_str
    return result

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = compress_string(sample_input)
    print(result)