def compress_rle(text):
    if not text:
        return ""
    
    compressed = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = text[i]
            count = 1
    
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    
    return "".join(compressed)

if __name__ == '__main__':
    sample_text = "AABBBCCCCCDD"
    result = compress_rle(sample_text)
    print(result)
    
    sample_text2 = "Hello World"
    result2 = compress_rle(sample_text2)
    print(result2)
    
    sample_text3 = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCC"
    result3 = compress_rle(sample_text3)
    print(result3)
    
    sample_text4 = ""
    result4 = compress_rle(sample_text4)
    print(result4)
    
    sample_text5 = "X"
    result5 = compress_rle(sample_text5)
    print(result5)