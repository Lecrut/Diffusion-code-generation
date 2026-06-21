def decompress_rle(compressed_string):
    if not compressed_string:
        return ""
    
    result = []
    i = 0
    n = len(compressed_string)
    
    while i < n:
        count_str = ""
        while i < n and compressed_string[i].isdigit():
            count_str += compressed_string[i]
            i += 1
        
        if i >= n:
            break
        
        char = compressed_string[i]
        count = int(count_str)
        result.append(char * count)
        i += 1
    
    return "".join(result)

if __name__ == "__main__":
    sample_compressed = "4a3b2c1d"
    original = decompress_rle(sample_compressed)
    print(original)