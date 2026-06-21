def rle_decode(compressed):
    if not compressed:
        return ""
    
    decoded = []
    i = 0
    n = len(compressed)
    
    while i < n:
        count_str = ""
        while i < n and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        
        if i < n:
            char = compressed[i]
            i += 1
            if count_str:
                count = int(count_str)
                decoded.append(char * count)
            else:
                decoded.append(char)
    
    return "".join(decoded)

if __name__ == "__main__":
    sample1 = "a3b2c1"
    result1 = rle_decode(sample1)
    print(result1)
    
    sample2 = "H2ello4"
    result2 = rle_decode(sample2)
    print(result2)
    
    sample3 = ""
    result3 = rle_decode(sample3)
    print(result3)
    
    sample4 = "x1y1z1"
    result4 = rle_decode(sample4)
    print(result4)