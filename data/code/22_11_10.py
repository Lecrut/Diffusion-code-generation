def decompress_rle(encoded_string):
    if not encoded_string:
        return ""
    
    result = []
    i = 0
    n = len(encoded_string)
    
    while i < n:
        char = encoded_string[i]
        i += 1
        
        count_str = []
        while i < n and encoded_string[i].isdigit():
            count_str.append(encoded_string[i])
            i += 1
        
        if count_str:
            count = int("".join(count_str))
        else:
            count = 1
        
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a4b2c10d1e1"
    output = decompress_rle(sample_input)
    print(output)