def compress_rle(text):
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
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    
    return "".join(result)

if __name__ == "__main__":
    sample_text = "AAAABBBCCDAA"
    compressed = compress_rle(sample_text)
    print(compressed)