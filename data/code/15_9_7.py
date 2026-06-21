def compress_string(input_str: str) -> str:
    if not input_str:
        return ""
    
    compressed = []
    current_char = input_str[0]
    count = 1
    
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
    
    result = "".join(compressed)
    
    if len(result) < len(input_str):
        return result
    
    return input_str

if __name__ == '__main__':
    original = 'aabcccccaaa'
    result = compress_string(original)
    print(result)