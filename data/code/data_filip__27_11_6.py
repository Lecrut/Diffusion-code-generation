def rle_encode(text):
    if not text:
        return ""
    
    encoded = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{current_char}")
            else:
                encoded.append(current_char)
            current_char = text[i]
            count = 1
    
    if count > 1:
        encoded.append(f"{count}{current_char}")
    else:
        encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_text = "aaabccccddde"
    result = rle_encode(sample_text)
    print(result)