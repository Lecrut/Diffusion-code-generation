def rle_compress(data):
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
            compressed.append(str(count) + current_char)
            current_char = char
            count = 1
            
    compressed.append(str(count) + current_char)
    
    return "".join(compressed)

def rle_decompress(data):
    if not data:
        return ""
    
    decompressed = []
    i = 0
    
    while i < len(data):
        count_str = []
        while i < len(data) and data[i].isdigit():
            count_str.append(data[i])
            i += 1
        
        if not count_str:
            decompressed.append(data[i])
            i += 1
        else:
            count = int("".join(count_str))
            char = data[i]
            decompressed.append(char * count)
            i += 1
            
    return "".join(decompressed)

if __name__ == '__main__':
    original_string = "AAABBBCCDDDDD"
    compressed_string = rle_compress(original_string)
    decompressed_string = rle_decompress(compressed_string)
    
    print(f"Original: {original_string}")
    print(f"Compressed: {compressed_string}")
    print(f"Decompressed: {decompressed_string}")