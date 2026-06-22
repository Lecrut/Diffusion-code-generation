def decompress_rle(compressed_string):
    if not compressed_string:
        return ""
    
    result = []
    i = 0
    length = len(compressed_string)
    
    while i < length:
        if not compressed_string[i].isdigit():
            raise ValueError(f"Invalid format: expected digit at index {i}, got '{compressed_string[i]}'")
        
        count_str = ""
        while i < length and compressed_string[i].isdigit():
            count_str += compressed_string[i]
            i += 1
        
        if i >= length:
            raise ValueError("Invalid format: missing character after count")
        
        char = compressed_string[i]
        count = int(count_str)
        
        result.append(char * count)
        i += 1
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "3a4b2c1d"
    original_string = decompress_rle(sample_input)
    print(original_string)