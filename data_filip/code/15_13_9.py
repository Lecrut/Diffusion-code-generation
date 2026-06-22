def compress_string(text: str) -> str:
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    length = len(text)
    
    for i in range(1, length):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = char
            count = 1
    
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    
    compressed = "".join(result)
    
    if len(compressed) < len(text):
        return compressed
    
    return text

if __name__ == '__main__':
    sample_text = "aaabbc"
    output = compress_string(sample_text)
    print(output)