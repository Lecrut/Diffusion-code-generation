def compress_string(input_str: str) -> str:
    if not input_str:
        return ""
    
    compressed = []
    count = 1
    current_char = input_str[0]
    
    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = input_str[i]
            count = 1
    
    compressed.append(f"{current_char}{count}")
    
    result = "".join(compressed)
    
    if len(result) < len(input_str):
        return result
    return input_str

if __name__ == '__main__':
    original = 'aabcccccaaa'
    result = compress_string(original)
    print(result)