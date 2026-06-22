import re

def rle_compress(text: str) -> str:
    if not text:
        return ""
    if len(text) < 2:
        return text + "1"
    
    compressed = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = char
            count = 1
            
    compressed.append(current_char)
    compressed.append(str(count))
    return "".join(compressed)

def rle_decompress(compressed: str) -> str:
    if not compressed:
        return ""
    
    decompressed = []
    i = 0
    length = len(compressed)
    
    while i < length:
        char = compressed[i]
        count_str = ""
        i += 1
        while i < length and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        
        if count_str:
            count = int(count_str)
            decompressed.append(char * count)
        else:
            decompressed.append(char)
            
    return "".join(decompressed)

if __name__ == '__main__':
    sample_text = "AAABBBCCCDD"
    compressed = rle_compress(sample_text)
    decompressed = rle_decompress(compressed)
    
    print(compressed)
    print(decompressed)