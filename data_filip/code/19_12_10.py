def rle_compress(text):
    if not text:
        return ""
    
    compressed = []
    current_char = text[0]
    count = 1
    length = len(text)
    
    for i in range(1, length):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 3:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = char
            count = 1
    
    if count > 3:
        compressed.append(str(count))
    compressed.append(current_char)
    
    return "".join(compressed)

def rle_decompress(compressed_text):
    if not compressed_text:
        return ""
    
    decompressed = []
    length = len(compressed_text)
    i = 0
    
    while i < length:
        char = compressed_text[i]
        if char.isdigit():
            j = i
            while j < length and compressed_text[j].isdigit():
                j += 1
            count = int(compressed_text[i:j])
            if j < length:
                next_char = compressed_text[j]
                decompressed.append(next_char * count)
                i = j + 1
            else:
                i += 1
        else:
            decompressed.append(char)
            i += 1
            
    return "".join(decompressed)

if __name__ == '__main__':
    original_text = "AAAAABBBCCCCCCDDDE"
    
    compressed = rle_compress(original_text)
    print(f"Compressed: {compressed}")
    
    decompressed = rle_decompress(compressed)
    print(f"Decompressed: {decompressed}")
    
    is_equal = original_text == decompressed
    print(f"Round-trip valid: {is_equal}")