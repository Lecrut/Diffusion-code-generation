def enhanced_rle_compress(data):
    if not data:
        return ""
    
    result = []
    i = 0
    n = len(data)
    escape_char = '\\'
    
    while i < n:
        current_char = data[i]
        count = 1
        
        while i + count < n and data[i + count] == current_char:
            count += 1
        
        if count == 1 and (current_char == escape_char or (current_char.isdigit() and int(current_char) < 10)):
            result.append(escape_char)
            result.append(current_char)
        elif count < 10:
            result.append(str(count))
            result.append(current_char)
        else:
            result.append(str(count))
            result.append(current_char)
        
        i += count
    
    return "".join(result)

def enhanced_rle_decompress(compressed_data):
    if not compressed_data:
        return ""
    
    result = []
    i = 0
    n = len(compressed_data)
    escape_char = '\\'
    
    while i < n:
        char = compressed_data[i]
        
        if char == escape_char and i + 1 < n:
            next_char = compressed_data[i + 1]
            result.append(next_char)
            i += 2
            continue
        
        if char.isdigit():
            count_str = char
            j = i + 1
            while j < n and compressed_data[j].isdigit():
                count_str += compressed_data[j]
                j += 1
            
            count = int(count_str)
            if j < n:
                result.append(compressed_data[j] * count)
                i = j + 1
            else:
                i = n
        else:
            result.append(char)
            i += 1
    
    return "".join(result)

if __name__ == '__main__':
    test_strings = [
        "AAAAAABCCCCCCCCD",
        "111222333",
        "a\\b\\c\\d",
        "AA\\BBCC",
        "RRRLLLLLL",
        ""
    ]
    
    for s in test_strings:
        compressed = enhanced_rle_compress(s)
        decompressed = enhanced_rle_decompress(compressed)
        print(f"Original: {s}")
        print(f"Compressed: {compressed}")
        print(f"Decompressed: {decompressed}")
        print(f"Match: {s == decompressed}")
        print("-" * 20)