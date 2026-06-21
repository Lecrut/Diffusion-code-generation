def rle_compress(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def rle_decompress(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    
    while i < len(data):
        num_str = []
        while i < len(data) and data[i].isdigit():
            num_str.append(data[i])
            i += 1
        
        if not num_str:
            raise ValueError("Invalid RLE string: expected a digit")
        
        count = int("".join(num_str))
        
        if i >= len(data) or not data[i].isdigit():
            char = data[i]
            i += 1
        else:
            raise ValueError("Invalid RLE string: expected a character after count")
        
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_data = "0011100"
    compressed = rle_compress(sample_data)
    print(compressed)
    decompressed = rle_decompress(compressed)
    print(decompressed)