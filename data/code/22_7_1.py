def rle_decode(compressed: str) -> str:
    if not compressed:
        return ""
    
    decoded_parts = []
    i = 0
    n = len(compressed)
    
    while i < n:
        count_str = ""
        while i < n and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        
        if i < n:
            char = compressed[i]
            i += 1
            decoded_parts.append(char * count)
        else:
            break
    
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_compressed = "3A2B5C1A"
    print(rle_decode(sample_compressed))
    
    sample_compressed2 = "12X4Y"
    print(rle_decode(sample_compressed2))
    
    sample_compressed3 = ""
    print(rle_decode(sample_compressed3))
    
    sample_compressed4 = "A"
    print(rle_decode(sample_compressed4))
    
    sample_compressed5 = "100Z"
    print(rle_decode(sample_compressed5))