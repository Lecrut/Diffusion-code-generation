def rle_compress(text: str) -> str:
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
            if count >= 3:
                result.append(str(count))
                result.append(current_char)
            elif count == 2:
                result.append(current_char)
                result.append(current_char)
            else:
                result.append(current_char)
            
            current_char = char
            count = 1
    
    if count >= 3:
        result.append(str(count))
        result.append(current_char)
    elif count == 2:
        result.append(current_char)
        result.append(current_char)
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbbccddeeeeff"
    compressed = rle_compress(sample_text)
    print(compressed)