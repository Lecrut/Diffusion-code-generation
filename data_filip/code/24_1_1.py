def rle_decompress(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    i = 0
    n = len(compressed)
    
    while i < n:
        count_str = ""
        while i < n and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        
        if i >= n:
            break
            
        char = compressed[i]
        count = int(count_str) if count_str else 1
        result.append(char * count)
        i += 1
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "3A2B4C1D"
    original_string = rle_decompress(sample_input)
    print(original_string)