def decompress_rle(s: str) -> str:
    if not s:
        return ""
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        char = s[i]
        i += 1
        
        if i >= n:
            result.append(char)
            continue
        
        count_str = []
        while i < n and s[i].isdigit():
            count_str.append(s[i])
            i += 1
        
        count = int("".join(count_str)) if count_str else 1
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a3b2c4"
    output = decompress_rle(sample_input)
    print(output)
    
    sample_input_2 = "A10B2"
    output_2 = decompress_rle(sample_input_2)
    print(output_2)
    
    sample_input_3 = "xyz10"
    output_3 = decompress_rle(sample_input_3)
    print(output_3)