def compress_rle(text):
    if not text:
        return ""
    
    compressed_chars = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed_chars.append(str(count))
            compressed_chars.append(current_char)
            current_char = text[i]
            count = 1
    
    compressed_chars.append(str(count))
    compressed_chars.append(current_char)
    
    return "".join(compressed_chars)

if __name__ == '__main__':
    sample_text = "AAABBBCCCDDD"
    result = compress_rle(sample_text)
    print(result)