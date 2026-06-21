def decompress_rle(encoded_string: str) -> str:
    if not encoded_string:
        return ""
    
    result = []
    i = 0
    n = len(encoded_string)
    
    while i < n:
        char = encoded_string[i]
        i += 1
        count_str = ""
        
        while i < n and encoded_string[i].isdigit():
            count_str += encoded_string[i]
            i += 1
        
        if count_str:
            count = int(count_str)
        else:
            count = 1
            
        result.append(char * count)
        
    return "".join(result)

if __name__ == '__main__':
    compressed = "a3b2c1d4"
    decompressed = decompress_rle(compressed)
    print(decompressed)