def decompress_rle(encoded_string: str) -> str:
    if not encoded_string:
        return ""
    
    result = []
    i = 0
    length = len(encoded_string)
    
    while i < length:
        char = encoded_string[i]
        i += 1
        count_str = ""
        while i < length and encoded_string[i].isdigit():
            count_str += encoded_string[i]
            i += 1
        
        if count_str:
            count = int(count_str)
            result.append(char * count)
        else:
            result.append(char)
            
    return "".join(result)

if __name__ == '__main__':
    sample_encoded = "a3b4c12"
    uncompressed = decompress_rle(sample_encoded)
    print(uncompressed)