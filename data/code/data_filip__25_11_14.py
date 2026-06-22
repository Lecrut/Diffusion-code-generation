def decompress_rle(encoded_str: str) -> str:
    result = []
    current_number = []
    
    for char in encoded_str:
        if char.isdigit():
            current_number.append(char)
        else:
            if current_number:
                count = int(''.join(current_number))
                current_number = []
                result.append(char * count)
            else:
                result.append(char)
                
    if current_number:
        count = int(''.join(current_number))
        result.append(char * count)
        
    return ''.join(result)

if __name__ == '__main__':
    encoded_input = "2a10b3c"
    original = decompress_rle(encoded_input)
    print(original)