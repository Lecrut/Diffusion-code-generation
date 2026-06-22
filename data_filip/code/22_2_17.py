def decompress_rle(encoded_str):
    if not encoded_str:
        return ""
    
    result = []
    current_digit = []
    
    for char in encoded_str:
        if char.isdigit():
            current_digit.append(char)
        else:
            if current_digit:
                count = int(''.join(current_digit))
                result.append(char * count)
                current_digit = []
            else:
                result.append(char)
    
    if current_digit:
        count = int(''.join(current_digit))
        result.append(result[-1] * (count - len(result[-1]) // len(result[-1]) if result else count))
    
    return "".join(result)

if __name__ == '__main__':
    encoded = "3a4b2c1d"
    result = decompress_rle(encoded)
    print(result)