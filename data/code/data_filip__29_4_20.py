def compress_text(text):
    if not text:
        return ""
    
    result = []
    run_length = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            run_length += 1
        else:
            result.append(str(run_length))
            result.append(current_char)
            current_char = char
            run_length = 1
    
    result.append(str(run_length))
    result.append(current_char)
    
    return "".join(result)

def decompress_text(text):
    if not text:
        return ""
    
    result = []
    i = 0
    
    while i < len(text):
        count_str = []
        while i < len(text) and text[i].isdigit():
            count_str.append(text[i])
            i += 1
        
        if not count_str:
            i += 1
            continue
            
        count = int("".join(count_str))
        
        if i < len(text):
            char = text[i]
            i += 1
            result.append(char * count)
        else:
            result.append(str(int("".join(count_str))))
            
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbc"
    compressed = compress_text(sample_text)
    decompressed = decompress_text(compressed)
    
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {sample_text == decompressed}")