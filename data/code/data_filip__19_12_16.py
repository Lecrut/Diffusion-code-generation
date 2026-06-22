def rle_encode(text):
    if not text:
        return ""
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

def rle_decode(encoded):
    if not encoded:
        return ""
    
    decoded = []
    i = 0
    while i < len(encoded):
        if encoded[i].isdigit():
            count = 0
            while i < len(encoded) and encoded[i].isdigit():
                count = count * 10 + int(encoded[i])
                i += 1
            if i < len(encoded):
                decoded.append(encoded[i] * count)
                i += 1
        else:
            decoded.append(encoded[i])
            i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    sample_text = "AAABBBCCDAA"
    encoded = rle_encode(sample_text)
    print(encoded)
    
    decoded = rle_decode(encoded)
    print(decoded)