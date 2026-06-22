def decode_rle(encoded: str) -> str:
    if not encoded:
        return ""
    
    result = []
    i = 0
    n = len(encoded)
    
    while i < n:
        char = encoded[i]
        i += 1
        
        if not char.isdigit():
            result.append(char)
            continue
        
        count_str = ""
        while i < n and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        
        if count <= 0:
            continue
        
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample1 = "2A3B4C"
    sample2 = "A1B1C1"
    sample3 = "10x"
    sample4 = ""
    sample5 = "A2"
    
    print(decode_rle(sample1))
    print(decode_rle(sample2))
    print(decode_rle(sample3))
    print(decode_rle(sample4))
    print(decode_rle(sample5))