def rle_compress(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
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

if __name__ == '__main__':
    sample_string = "AAABBBCCCD"
    compressed = rle_compress(sample_string)
    print(compressed)