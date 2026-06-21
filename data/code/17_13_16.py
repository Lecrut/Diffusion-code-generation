def rle_encode(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)
    
    return "".join(result)

def rle_decode(text):
    if not text:
        return ""
    
    result = []
    i = 0
    length = len(text)
    
    while i < length:
        if text[i].isdigit():
            j = i
            while j < length and text[j].isdigit():
                j += 1
            count = int(text[i:j])
            if j < length:
                result.append(text[j] * count)
                i = j + 1
            else:
                i = j
        else:
            result.append(text[i])
            i += 1
    
    return "".join(result)

if __name__ == '__main__':
    encoded = rle_encode("AAABBBCCCD")
    print(encoded)
    
    decoded = rle_decode(encoded)
    print(decoded)