def rle_decompress(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    i = 0
    n = len(compressed)
    
    while i < n:
        char = compressed[i]
        i += 1
        
        if not char.isdigit():
            result.append(char)
            continue
            
        count_str = []
        while i < n and compressed[i].isdigit():
            count_str.append(compressed[i])
            i += 1
        
        if not count_str:
            result.append(char)
        else:
            count = int("".join(count_str))
            result.append(char * count)
            
    return "".join(result)

if __name__ == '__main__':
    compressed_data = "3a4b2c1d"
    original = rle_decompress(compressed_data)
    print(original)