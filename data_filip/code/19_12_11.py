import sys

def rle_compress(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    length = len(text)
    
    i = 1
    while i < length:
        char = text[i]
        if char == current_char:
            count += 1
            if count == 9:
                result.append(str(count))
                result.append(current_char)
                count = 0
        else:
            if count > 0:
                result.append(str(count))
                result.append(current_char)
            current_char = char
            count = 1
        i += 1
    
    if count > 0:
        result.append(str(count))
        result.append(current_char)
        
    return "".join(result)

def rle_decompress(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    length = len(compressed)
    i = 0
    
    while i < length:
        char_count = 0
        while i < length and compressed[i].isdigit():
            char_count = char_count * 10 + int(compressed[i])
            i += 1
        
        if i < length:
            count_char = compressed[i]
            result.append(count_char * char_count)
            i += 1
            
    return "".join(result)

def run_demo():
    original = "AAABBBCCCD"
    compressed = rle_compress(original)
    decompressed = rle_decompress(compressed)
    
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {original == decompressed}")

if __name__ == '__main__':
    run_demo()