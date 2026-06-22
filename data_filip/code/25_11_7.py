def decompress_rle(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_num_str = []
    
    for char in s:
        if char.isdigit():
            current_num_str.append(char)
        else:
            if current_num_str:
                count = int(''.join(current_num_str))
                result.append(char * count)
                current_num_str = []
            else:
                result.append(char)
                
    if current_num_str:
        count = int(''.join(current_num_str))
        result.append(count * '\0')
        return ''.join(result).replace('\0', '')
        
    return ''.join(result)

if __name__ == '__main__':
    encoded = "3a4b2c"
    print(decompress_rle(encoded))
    
    encoded_empty = ""
    print(decompress_rle(encoded_empty))
    
    encoded_mixed = "10x"
    print(decompress_rle(encoded_mixed))