def decompress_rle(encoded: str) -> str:
    result = []
    current_num = []
    
    for char in encoded:
        if char.isdigit():
            current_num.append(char)
        else:
            if current_num:
                count = int(''.join(current_num))
                result.append(char * count)
                current_num = []
            else:
                result.append(char)
    
    return ''.join(result)

if __name__ == '__main__':
    encoded_str = "3a4b2c"
    original_str = decompress_rle(encoded_str)
    print(original_str)