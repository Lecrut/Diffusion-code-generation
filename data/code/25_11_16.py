def decompress_rle(encoded: str) -> str:
    if not encoded:
        return ""
    
    result = []
    count = 0
    
    for char in encoded:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            if count == 0:
                count = 1
            result.append(char * count)
            count = 0
            
    return "".join(result)

if __name__ == '__main__':
    sample_input = "3a4b2c"
    decompressed = decompress_rle(sample_input)
    print(decompressed)