def compress_string(text: str) -> str:
    if not text:
        return ""
    
    if len(text) == 1:
        return text
    
    result_parts = []
    current_char = text[0]
    count = 1
    
    i = 1
    while i < len(text):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result_parts.append(current_char + str(count))
            else:
                result_parts.append(current_char)
            current_char = char
            count = 1
        i += 1
    
    if count > 1:
        result_parts.append(current_char + str(count))
    else:
        result_parts.append(current_char)
    
    return "".join(result_parts)

if __name__ == '__main__':
    sample_text = "aaabbc"
    compressed = compress_string(sample_text)
    print(compressed)