def compress_string(input_string):
    if not input_string:
        return ""
    
    compressed = []
    count = 1
    current_char = input_string[0]
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed.append(f"{current_char}{count}")
    
    result = "".join(compressed)
    return result if len(result) < len(input_string) else input_string

if __name__ == '__main__':
    sample = 'aabbccc'
    result = compress_string(sample)
    print(result)