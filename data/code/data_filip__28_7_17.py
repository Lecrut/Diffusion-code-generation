def rle_encode(text):
    if not text:
        return ""
    
    encoded = []
    count = 0
    prev_char = text[0]
    
    for char in text:
        if char == prev_char:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{prev_char}")
            else:
                encoded.append(prev_char)
            prev_char = char
            count = 1
    
    if count > 1:
        encoded.append(f"{count}{prev_char}")
    else:
        encoded.append(prev_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    result = rle_encode(sample_text)
    print(result)