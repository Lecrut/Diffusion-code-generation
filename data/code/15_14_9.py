def compress_string(text):
    if not text:
        return ""
    
    compressed = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = text[i]
            count = 1
            
    compressed.append(current_char)
    compressed.append(str(count))
    
    return "".join(compressed)

if __name__ == '__main__':
    input_str = "aaabbc"
    result = compress_string(input_str)
    print(result)