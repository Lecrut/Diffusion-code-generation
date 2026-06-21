def compress_text(text: str) -> str:
    if not text:
        return ""
    
    result_parts = []
    current_char = text[0]
    count = 1
    length = len(text)
    
    i = 1
    while i < length:
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count == 1:
                result_parts.append(current_char)
            else:
                result_parts.append(str(count))
                result_parts.append(current_char)
            current_char = char
            count = 1
        i += 1
    
    if count == 1:
        result_parts.append(current_char)
    else:
        result_parts.append(str(count))
        result_parts.append(current_char)
    
    return "".join(result_parts)

if __name__ == '__main__':
    sample = "aaabbbccdddeff"
    compressed = compress_text(sample)
    print(compressed)