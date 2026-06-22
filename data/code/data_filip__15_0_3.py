def compress_string(input_str):
    if not input_str:
        return ""
    
    compressed = []
    count = 1
    current_char = input_str[0]
    
    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = input_str[i]
            count = 1
    
    compressed.append(current_char)
    compressed.append(str(count))
    
    compressed_str = "".join(compressed)
    
    if len(compressed_str) >= len(input_str):
        return input_str
    
    return compressed_str

if __name__ == '__main__':
    input_text = "aabcccccaaa"
    result = compress_string(input_text)
    print(result)