def enhanced_rle_compress(data: str) -> str:
    if not data:
        return ""
    
    compressed = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = char
            count = 1
    compressed.append(f"{count}{current_char}")
    
    return "".join(compressed)

def enhanced_rle_depress(data: str) -> str:
    if not data:
        return ""
    
    decompressed = []
    i = 0
    n = len(data)
    
    while i < n:
        count_str = ""
        while i < n and data[i].isdigit():
            count_str += data[i]
            i += 1
        
        if not count_str:
            raise ValueError("Invalid RLE format: missing count")
            
        if i >= n:
            raise ValueError("Invalid RLE format: missing character")
            
        char = data[i]
        count = int(count_str)
        decompressed.append(char * count)
        i += 1
        
    return "".join(decompressed)

if __name__ == '__main__':
    original = "AAABBBCCDDA"
    compressed = enhanced_rle_compress(original)
    decompressed = enhanced_rle_depress(compressed)
    print(original)
    print(compressed)
    print(decompressed)