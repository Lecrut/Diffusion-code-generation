def decompress_rle(encoded_string):
    if not encoded_string:
        return ""
    
    result = []
    i = 0
    n = len(encoded_string)
    
    while i < n:
        char = encoded_string[i]
        i += 1
        if i >= n or not encoded_string[i].isdigit():
            result.append(char)
            continue
        
        count_str = []
        while i < n and encoded_string[i].isdigit():
            count_str.append(encoded_string[i])
            i += 1
        
        count = int("".join(count_str))
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a3b2c1"
    decompressed = decompress_rle(sample_input)
    print(decompressed)
    
    sample_input_2 = "x10y5z3"
    decompressed_2 = decompress_rle(sample_input_2)
    print(decompressed_2)
    
    sample_input_3 = "A1B2C3D4"
    decompressed_3 = decompress_rle(sample_input_3)
    print(decompressed_3)