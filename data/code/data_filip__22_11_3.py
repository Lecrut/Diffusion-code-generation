def decompress_rle(encoded: str) -> str:
    if not encoded:
        return ""
    
    result = []
    i = 0
    length = len(encoded)
    
    while i < length:
        char = encoded[i]
        i += 1
        
        if i < length and encoded[i].isdigit():
            num_str = ""
            while i < length and encoded[i].isdigit():
                num_str += encoded[i]
                i += 1
            count = int(num_str)
            result.append(char * count)
        else:
            result.append(char)
            
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a2b3c1d4"
    uncompressed = decompress_rle(sample_input)
    print(uncompressed)