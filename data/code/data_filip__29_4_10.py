def compress_text(text: str) -> str:
    if not text:
        return ""
    
    result = []
    length = len(text)
    index = 0
    
    while index < length:
        current_char = text[index]
        count = 1
        
        while index + count < length and text[index + count] == current_char:
            count += 1
        
        if count >= 4:
            result.append(str(count))
            result.append(current_char)
            index += count
        else:
            result.append(current_char)
            index += 1
            
    return ''.join(result)

def decompress_text(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    length = len(compressed)
    index = 0
    
    while index < length:
        char = compressed[index]
        
        if char.isdigit():
            count_str = char
            while index + 1 < length and compressed[index + 1].isdigit():
                index += 1
                count_str += compressed[index]
            repeat_count = int(count_str)
            
            if index + 1 < length:
                index += 1
                current_char = compressed[index]
                result.append(current_char * repeat_count)
            else:
                result.append(char)
        else:
            result.append(char)
        
        index += 1
        
    return ''.join(result)

if __name__ == '__main__':
    original = "aabcccccaaa"
    compressed = compress_text(original)
    print(compressed)
    decompressed = decompress_text(compressed)
    print(decompressed)