def compress_string(input_string: str) -> str:
    if not input_string:
        return ""
    
    compressed = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = input_string[i]
            count = 1
    
    compressed.append(f"{current_char}{count}")
    
    result = "".join(compressed)
    
    if len(result) < len(input_string):
        return result
    else:
        return input_string

if __name__ == '__main__':
    original = 'aabcccccaaa'
    compressed_result = compress_string(original)
    print(compressed_result)