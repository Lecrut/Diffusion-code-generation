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
    index = 0
    
    while index < len(data):
        count_str = []
        while index < len(data) and data[index].isdigit():
            count_str.append(data[index])
            index += 1
        
        if index < len(data):
            count = int("".join(count_str))
            char = data[index]
            result.append(char * count)
            index += 1
            
    return "".join(result)

if __name__ == "__main__":
    sample_data = "0011100"
    
    compressed = rle_compress(sample_data)
    print(compressed)
    
    decompressed = rle_decompress(compressed)
    print(decompressed)