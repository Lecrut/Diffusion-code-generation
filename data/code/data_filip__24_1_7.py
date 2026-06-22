def decompress_rle(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    current_digit = []
    
    for char in compressed:
        if char.isdigit():
            current_digit.append(char)
        else:
            if current_digit:
                count = int("".join(current_digit))
                result.append(char * count)
                current_digit = []
            else:
                result.append(char)
    
    if current_digit:
        count = int("".join(current_digit))
        result.append("*" * count)
    
    return "".join(result)

if __name__ == '__main__':
    compressed_data = "a3b1c5d2"
    decompressed = decompress_rle(compressed_data)
    print(decompressed)