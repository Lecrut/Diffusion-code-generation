def bidirectional_rle(text):
    if not text:
        return ""
    
    compressed_parts = []
    count = 1
    char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == char:
            count += 1
        else:
            compressed_parts.append(str(count) + char)
            char = text[i]
            count = 1
    compressed_parts.append(str(count) + char)
    compressed = "".join(compressed_parts)
    
    decompressed_parts = []
    j = 0
    while j < len(compressed):
        num_str = ""
        while j < len(compressed) and compressed[j].isdigit():
            num_str += compressed[j]
            j += 1
        if j < len(compressed):
            char = compressed[j]
            count = int(num_str)
            decompressed_parts.append(char * count)
            j += 1
    decompressed = "".join(decompressed_parts)
    
    if text == decompressed:
        return compressed
    else:
        return None

if __name__ == '__main__':
    sample_input = "aaabbcccc"
    result = bidirectional_rle(sample_input)
    print(result)